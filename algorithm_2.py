from AlgorithmImports import *
from datetime import timedelta
import pandas as pd

from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

class MarkovVolatilityStopLossModel(QCAlgorithm):
    """
    This algorithm places a market order on the first trading day of each week. 
    The default stop loss is set at .95 of the price (allowing <= 5% loss) 
    If the markov model detects a regime shift, the stop loss is changed depending on the current 
    predicted regime. The algorithm is set to change the stop loss to .98 for low volatility regimes
    and .95 for low volatility ones. If the stop loss isn't hit by the end of the week, the algorithm 
    automatically cancels it and liquidates the position. A new order is placed at the beginning
    of each week with the updated stop loss for the most recently predicted regime.
    """

    def initialize(self):
        self.set_start_date(2018, 12, 31)
        self.set_end_date(2024, 12, 31)
        self.set_cash(100_000)
        self._security = self.add_equity("AAPL")
        self._symbol = self._security.symbol


        self._stop_loss_percent = self.get_parameter("stop_loss_percent", 0.95)

        self._lookback_period = timedelta(
            self.get_parameter('lookback_years', 3) * 365
        )


        self._daily_returns = pd.Series()
        roc = self.roc(self._symbol, 1, Resolution.DAILY)
        roc.updated += self._update_event_handler
        history = self.history[TradeBar](
            self._symbol, self._lookback_period + timedelta(7), Resolution.DAILY
        )
        for bar in history:
            roc.update(bar.end_time, bar.close)

        self.schedule.on(
            self.date_rules.every_day(self._symbol),
            self.time_rules.before_market_open(self._symbol, 10),
            self._predict_regime
        )

        self.schedule.on(
            self.date_rules.week_start(self._symbol),
            self.time_rules.after_market_open(self._symbol, 2),
            self._enter
        )

        self.schedule.on(
            self.date_rules.week_end(self._symbol),
            self.time_rules.before_market_close(self._symbol, 30),
            self.liquidate
        )
        self._previous_regime = None

    def _update_event_handler(self, indicator, indicator_data_point):
        if not indicator.is_ready:
            return
        t = indicator_data_point.end_time
        self._daily_returns.loc[t] = indicator_data_point.value
        self._daily_returns = self._daily_returns[
            t - self._daily_returns.index <= self._lookback_period
        ]

    def _enter(self):
        quantity = self.calculate_order_quantity(self._symbol, 1)
        self.market_order(self._symbol, quantity)
        self.stop_market_order(
            self._symbol, -quantity,
            round(self._security.price * self._stop_loss_percent, 2)
        )

    def _predict_regime(self):
        model = MarkovRegression(
            self._daily_returns, k_regimes=2, switching_variance=True
        )

        regime = model.fit().smoothed_marginal_probabilities.values\
            .argmax(axis=1)[-1]
        self.plot('Regime', 'Volatility Class', regime)

        if regime == 0:
              self._stop_loss_percent = .98
        elif regime == 1:
              self._stop_loss_percent = .95