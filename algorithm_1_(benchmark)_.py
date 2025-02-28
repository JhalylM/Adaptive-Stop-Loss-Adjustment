from AlgorithmImports import *


class MarkovVolatilityBenchmark(QCAlgorithm):
    """
    This algorithm serves as a benchmark for the main algorithm.
    It buys a fixed portion of Apple stock at the beginning of
    every week, and liquidates at the end of every week.
    """

    def initialize(self):
        self.set_start_date(2018, 12, 31)
        self.set_end_date(2024, 12, 31)
        self.set_cash(100_000)
        self._security = self.add_equity("AAPL")
        self._symbol = self._security.symbol

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

    def _enter(self):
        quantity = self.calculate_order_quantity(self._symbol, 1)
        self.market_order(self._symbol, quantity)