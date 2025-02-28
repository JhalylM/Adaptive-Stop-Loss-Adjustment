# Adaptive Stop Loss Adjustment with Markov Switching Volatility Regimes

## **Overview**

This project explores adaptive stop-loss strategies for trading Apple Inc. (AAPL) stock by dynamically adjusting stop levels based on volatility regimes predicted by a Markov switching model. The objective is to test whether such adaptive methods can improve risk-adjusted performance compared to a simple weekly rebalancing strategy.

## **Objective**

The goal of this project is to use a Markov Switching Regression model to classify detected market regimes into two classes based on volatility: high and low. The strategy then implements adaptive stop losses that adjust based on the detected regime to optimize risk management and performance.

## **Motivation**

In financial markets, volatility is a key driver of asset price behavior. Understanding and anticipating changes in volatility is critical for implementing effective risk management strategies. Volatility can be broadly classified into low and high regimes, each of which influences market behavior differently:

Low volatility regimes are typically characterized by more stable and predictable price movements. In these periods, assets tend to exhibit steady trends, and prices are less likely to experience sudden, sharp reversals. 

High volatility regimes, on the other hand, are marked by larger price fluctuations and more erratic market movements. During these periods, sudden reversals and sharp market swings are more common, which increases the risk of large losses. 

The motivation for this project is to develop a more adaptive and responsive trading strategy that adjusts to these changing market conditions. By implementing a stop-loss strategy that adapts to market volatility, the objective is to reduce exposure during periods of high volatility (when markets are riskier) and provide more flexibility during periods of low volatility, thereby optimizing risk management and improving overall portfolio performance.

## **Data & Methodology**

**Data:** Historical Apple stock data from 2019–2025 was used for backtesting the strategy.

**Portfolio:** The portfolio is 100% weighted in Apple stock, with purchases made at the beginning of each week.

**Markov Model:** The Markov Switching Regression model is trained daily, 10 minutes before the market open, to classify market volatility regimes as either high or low.

**Stop-Loss Adjustments:** Stop-loss adjustments are made at the beginning of each week with the new purchase of stocks, based on the volatility regime detected by the Markov model.

## **Trading Algorithms Tested**

## **Algorithm 1 (Benchmark):**

Buys a fixed amount of AAPL at the beginning of every week and sells at the week’s end.

## **Algorithm 2:**

Uses a default stop-loss of 0.95 (95% of the original purchase price) and adjusts the stop loss based on the volatility regime predicted by the Markov model: 0.98 (98% of purchase price) for low volatility and 0.95 for high volatility.

## **Algorithm 3:**

Similar to Algorithm 2 but reverses the stop-loss values: 0.95 for low volatility and 0.98 for high volatility.

## **Performance Results**

**Algorithm 1 (Benchmark):**

**Sharpe:** 1.169 | **Avg Win \%:** 2.9% | **Max Drawdown:** 23.4% | **Annual Return:** 40.17% | **Net Profit:** 637.89% | **Win Rate:** 59%

**Algorithm 2:**

**Sharpe:** 0.76 | **Avg Win %:** 2.54% | **Max Drawdown:** 33.9% | **Annual Return:** 22.3% | **Net Profit:** 229.23% | **Win Rate:** 54%

**Algorithm 3:**

**Sharpe:** 0.898 | **Avg Win %:** 2.45% | **Max Drawdown:** 28.6% | **Annual Return:** 27.29% | **Net Profit:** 317.14% | **Win Rate:** 59%

## **Conclusion**

The results of this study indicate that a volatility-adaptive stop-loss strategy can reduce risk exposure in high-volatility regimes, but it does not necessarily outperform a simple buy-and-hold strategy in terms of long-term performance metrics such as the Sharpe ratio and net profit. In particular, Algorithm 1 (the benchmark strategy) outperformed the adaptive strategies across most metrics, including annual return, net profit, and risk-adjusted returns. This suggests that while adaptive stop losses offer potential benefits in managing risk, they may also lead to missed opportunities during periods of lower volatility when the market is trending.

However, it is important to note that Algorithm 3, which reversed the stop-loss values for low and high volatility, showed better results in terms of net profit compared to Algorithm 2, highlighting the potential for optimization in stop-loss settings.

Overall, the results underscore the importance of volatility regime detection and demonstrate that further refinement and fine-tuning of the strategy may lead to improved performance.

## **Future Work**

While this study provides insight into the potential of volatility-based adaptive stop-loss strategies, there are several areas for further exploration:

**Refining the Markov Switching Model:**

The current Markov model uses basic training to classify volatility regimes, but more advanced techniques could be explored. For instance, improving the feature set used for regime classification (e.g., using additional technical indicators or machine learning models) could lead to more accurate regime detection and better performance.

**Alternative Stop-Loss Strategies:**

Testing different stop-loss thresholds or exploring dynamic adjustments based on the ATR (Average True Range) or other volatility measures could further optimize risk management. For example, experimenting with a trailing stop-loss that moves in sync with price trends could help lock in profits during trending markets.

**Testing on Other Assets or Markets:**

Expanding the study to other assets or markets would allow for a more comprehensive understanding of how volatility-adaptive strategies perform across different securities. For example, testing on more volatile stocks, ETFs, or even cryptocurrencies could highlight differences in how the strategy adapts to market conditions.

## Overall
By continuing to refine the volatility-adaptive stop-loss strategy and exploring these areas, it is possible to improve both performance and risk management in dynamic financial markets.
