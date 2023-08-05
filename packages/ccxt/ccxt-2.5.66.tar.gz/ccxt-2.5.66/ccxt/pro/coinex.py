# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.pro.base.exchange import Exchange
import ccxt.async_support
from ccxt.pro.base.cache import ArrayCache, ArrayCacheBySymbolById, ArrayCacheByTimestamp
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import BadRequest
from ccxt.base.errors import NotSupported
from ccxt.base.errors import ExchangeNotAvailable
from ccxt.base.errors import RequestTimeout
from ccxt.base.precise import Precise


class coinex(Exchange, ccxt.async_support.coinex):

    def describe(self):
        return self.deep_extend(super(coinex, self).describe(), {
            'has': {
                'ws': True,
                'watchBalance': True,
                'watchTicker': True,
                'watchTickers': False,
                'watchTrades': True,
                'watchMyTrades': False,  # can query but can't subscribe
                'watchOrders': True,
                'watchOrderBook': True,
                'watchOHLCV': False,  # only for swap markets
            },
            'urls': {
                'api': {
                    'ws': {
                        'spot': 'wss://socket.coinex.com/',
                        'swap': 'wss://perpetual.coinex.com/',
                    },
                },
            },
            'options': {
                'account': 'spot',
                'watchOrderBook': {
                    'limits': [5, 10, 20, 50],
                    'defaultLimit': 50,
                    'aggregations': ['10', '1', '0', '0.1', '0.01'],
                    'defaultAggregation': '0',
                },
            },
            'streaming': {
            },
            'exceptions': {
                'codes': {
                    '1': BadRequest,  # Parameter error
                    '2': ExchangeError,  # Internal error
                    '3': ExchangeNotAvailable,  # Service unavailable
                    '4': NotSupported,  # Method unavailable
                    '5': RequestTimeout,  # Service timeout
                    '6': AuthenticationError,  # Permission denied
                },
            },
            'timeframes': {
                '1m': 60,
                '3m': 180,
                '5m': 300,
                '15m': 900,
                '30m': 1800,
                '1h': 3600,
                '2h': 7200,
                '4h': 14400,
                '6h': 21600,
                '12h': 43200,
                '1d': 86400,
                '3d': 259200,
                '1w': 604800,
            },
        })

    def request_id(self):
        requestId = self.sum(self.safe_integer(self.options, 'requestId', 0), 1)
        self.options['requestId'] = requestId
        return requestId

    def handle_ticker(self, client, message):
        #
        #  spot
        #
        #     {
        #         method: 'state.update',
        #         params: [{
        #             BTCUSDT: {
        #                 last: '31577.89',
        #                 open: '29318.36',
        #                 close: '31577.89',
        #                 high: '32222.19',
        #                 low: '29317.21',
        #                 volume: '630.43024965',
        #                 sell_total: '13.66143951',
        #                 buy_total: '2.76410939',
        #                 period: 86400,
        #                 deal: '19457487.84611409070000000000'
        #             }
        #         }]
        #     }
        #
        #  swap
        #
        #     {
        #         method: 'state.update',
        #         params: [{
        #             BTCUSDT: {
        #                 period: 86400,
        #                 funding_time: 422,
        #                 position_amount: '285.6246',
        #                 funding_rate_last: '-0.00097933',
        #                 funding_rate_next: '0.00022519',
        #                 funding_rate_predict: '0.00075190',
        #                 insurance: '17474289.49925859030905338270',
        #                 last: '31570.08',
        #                 sign_price: '31568.09',
        #                 index_price: '31561.85000000',
        #                 open: '29296.11',
        #                 close: '31570.08',
        #                 high: '32463.40',
        #                 low: '29296.11',
        #                 volume: '8774.7318',
        #                 deal: '270675177.827928219109030017258398',
        #                 sell_total: '19.2230',
        #                 buy_total: '25.7814'
        #             }
        #         }]
        #     }
        #
        params = self.safe_value(message, 'params', [])
        first = self.safe_value(params, 0, {})
        keys = list(first.keys())
        marketId = self.safe_string(keys, 0)
        symbol = self.safe_symbol(marketId)
        ticker = self.safe_value(first, marketId, {})
        market = self.safe_market(marketId)
        parsedTicker = self.parse_ws_ticker(ticker, market)
        messageHash = 'ticker:' + symbol
        self.tickers[symbol] = parsedTicker
        client.resolve(parsedTicker, messageHash)

    def parse_ws_ticker(self, ticker, market=None):
        #
        #  spot
        #
        #     {
        #         last: '31577.89',
        #         open: '29318.36',
        #         close: '31577.89',
        #         high: '32222.19',
        #         low: '29317.21',
        #         volume: '630.43024965',
        #         sell_total: '13.66143951',
        #         buy_total: '2.76410939',
        #         period: 86400,
        #         deal: '19457487.84611409070000000000'
        #     }
        #
        #  swap
        #
        #     {
        #         period: 86400,
        #         funding_time: 422,
        #         position_amount: '285.6246',
        #         funding_rate_last: '-0.00097933',
        #         funding_rate_next: '0.00022519',
        #         funding_rate_predict: '0.00075190',
        #         insurance: '17474289.49925859030905338270',
        #         last: '31570.08',
        #         sign_price: '31568.09',
        #         index_price: '31561.85000000',
        #         open: '29296.11',
        #         close: '31570.08',
        #         high: '32463.40',
        #         low: '29296.11',
        #         volume: '8774.7318',
        #         deal: '270675177.827928219109030017258398',
        #         sell_total: '19.2230',
        #         buy_total: '25.7814'
        #     }
        #
        return self.safe_ticker({
            'symbol': self.safe_symbol(None, market),
            'timestamp': None,
            'datetime': None,
            'high': self.safe_string(ticker, 'high'),
            'low': self.safe_string(ticker, 'low'),
            'bid': None,
            'bidVolume': self.safe_string(ticker, 'buy_total'),
            'ask': None,
            'askVolume': self.safe_string(ticker, 'sell_total'),
            'vwap': None,
            'open': self.safe_string(ticker, 'open'),
            'close': self.safe_string(ticker, 'close'),
            'last': self.safe_string(ticker, 'last'),
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_string(ticker, 'volume'),
            'quoteVolume': self.safe_string(ticker, 'deal'),
            'info': ticker,
        }, market)

    async def watch_balance(self, params={}):
        """
        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict params: extra parameters specific to the coinex api endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/en/latest/manual.html?#balance-structure>`
        """
        await self.load_markets()
        await self.authenticate(params)
        messageHash = 'balance'
        type = None
        type, params = self.handle_market_type_and_params('watchBalance', None, params)
        url = self.urls['api']['ws'][type]
        currencies = list(self.currencies_by_id.keys())
        subscribe = {
            'method': 'asset.subscribe',
            'params': currencies,
            'id': self.request_id(),
        }
        request = self.deep_extend(subscribe, params)
        return await self.watch(url, messageHash, request, messageHash)

    def handle_balance(self, client, message):
        #
        #     {
        #         "method": "asset.update",
        #         "params": [
        #             {
        #                 "BTC": {
        #                     "available": "250",
        #                     "frozen": "10",
        #                 }
        #             }
        #         ],
        #         "id": null
        #     }
        #
        params = self.safe_value(message, 'params', [])
        first = self.safe_value(params, 0, {})
        currencies = list(first.keys())
        for i in range(0, len(currencies)):
            currencyId = currencies[i]
            code = self.safe_currency_code(currencyId)
            available = self.safe_string(first[currencyId], 'available')
            frozen = self.safe_string(first[currencyId], 'frozen')
            total = Precise.string_add(available, frozen)
            account = self.account()
            account['free'] = self.parse_number(available)
            account['used'] = self.parse_number(frozen)
            account['total'] = self.parse_number(total)
            self.balance[code] = account
            self.balance = self.safe_balance(self.balance)
        messageHash = 'balance'
        client.resolve(self.balance, messageHash)

    def handle_trades(self, client, message):
        #
        #     {
        #         "method": "deals.update",
        #         "params": [
        #             "BTCUSD",
        #             [{
        #                 "type": "sell",
        #                 "time": 1496458040.059284,
        #                 "price ": "46444.74",
        #                 "id": 29433,
        #                 "amount": "0.00120000"
        #             }]
        #         ],
        #         "id": null
        #     }
        #
        params = self.safe_value(message, 'params', [])
        marketId = self.safe_string(params, 0)
        trades = self.safe_value(params, 1, [])
        market = self.safe_market(marketId)
        symbol = self.safe_symbol(marketId)
        messageHash = 'trades:' + symbol
        stored = self.safe_value(self.trades, symbol)
        if stored is None:
            limit = self.safe_integer(self.options, 'tradesLimit', 1000)
            stored = ArrayCache(limit)
            self.trades[symbol] = stored
        for i in range(0, len(trades)):
            trade = trades[i]
            parsed = self.parse_ws_trade(trade, market)
            stored.append(parsed)
        self.trades[symbol] = stored
        client.resolve(self.trades[symbol], messageHash)

    def parse_ws_trade(self, trade, market=None):
        #
        #     {
        #         "type": "sell",
        #         "time": 1496458040.059284,
        #         "price ": "46444.74",
        #         "id": 29433,
        #         "amount": "0.00120000"
        #     }
        #
        timestamp = self.safe_timestamp(trade, 'time')
        return self.safe_trade({
            'id': self.safe_string(trade, 'id'),
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': self.safe_symbol(None, market),
            'order': None,
            'type': None,
            'side': self.safe_string(trade, 'type'),
            'takerOrMaker': None,
            'price': self.safe_string(trade, 'price'),
            'amount': self.safe_string(trade, 'amount'),
            'cost': None,
            'fee': None,
        }, market)

    def handle_ohlcv(self, client, message):
        #
        #     {
        #         method: 'kline.update',
        #         params: [
        #             [
        #                 1654019640,   # timestamp
        #                 '32061.99',   # open
        #                 '32061.28',   # close
        #                 '32061.99',   # high
        #                 '32061.28',   # low
        #                 '0.1285',     # amount base
        #                 '4119.943736'  # amount quote
        #             ]
        #         ],
        #         id: null
        #     }
        #
        candles = self.safe_value(message, 'params', [])
        messageHash = 'ohlcv'
        ohlcvs = self.parse_ohlcvs(candles)
        if self.ohlcvs == 0:
            limit = self.safe_integer(self.options, 'OHLCVLimit', 1000)
            self.ohlcvs = ArrayCacheByTimestamp(limit)
        for i in range(0, len(ohlcvs)):
            candle = ohlcvs[i]
            self.ohlcvs.append(candle)
        client.resolve(self.ohlcvs, messageHash)

    async def watch_ticker(self, symbol, params={}):
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict params: extra parameters specific to the coinex api endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/en/latest/manual.html#ticker-structure>`
        """
        await self.load_markets()
        market = self.market(symbol)
        type = None
        type, params = self.handle_market_type_and_params('watchTicker', market, params)
        url = self.urls['api']['ws'][type]
        messageHash = 'ticker:' + symbol
        subscribe = {
            'method': 'state.subscribe',
            'id': self.request_id(),
            'params': [
                market['id'],
            ],
        }
        request = self.deep_extend(subscribe, params)
        return await self.watch(url, messageHash, request, messageHash, request)

    async def watch_trades(self, symbol, since=None, limit=None, params={}):
        """
        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int|None since: timestamp in ms of the earliest trade to fetch
        :param int|None limit: the maximum amount of trades to fetch
        :param dict params: extra parameters specific to the coinex api endpoint
        :returns [dict]: a list of `trade structures <https://docs.ccxt.com/en/latest/manual.html?#public-trades>`
        """
        await self.load_markets()
        market = self.market(symbol)
        symbol = market['symbol']
        type = None
        type, params = self.handle_market_type_and_params('watchTrades', market, params)
        url = self.urls['api']['ws'][type]
        messageHash = 'trades:' + symbol
        message = {
            'method': 'deals.subscribe',
            'params': [
                market['id'],
            ],
            'id': self.request_id(),
        }
        request = self.deep_extend(message, params)
        trades = await self.watch(url, messageHash, request, messageHash, request)
        return self.filter_by_since_limit(trades, since, limit, 'timestamp', True)

    async def watch_order_book(self, symbol, limit=None, params={}):
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int|None limit: the maximum amount of order book entries to return
        :param dict params: extra parameters specific to the coinex api endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/en/latest/manual.html#order-book-structure>` indexed by market symbols
        """
        await self.load_markets()
        market = self.market(symbol)
        symbol = market['symbol']
        type = None
        type, params = self.handle_market_type_and_params('watchOrderBook', market, params)
        url = self.urls['api']['ws'][type]
        name = 'orderbook'
        messageHash = name + ':' + symbol
        options = self.safe_value(self.options, 'watchOrderBook', {})
        limits = self.safe_value(options, 'limits', [])
        if limit is None:
            limit = self.safe_value(options, 'defaultLimit', 50)
        if not self.in_array(limit, limits):
            raise NotSupported(self.id + ' watchOrderBook() limit must be one of ' + ', '.join(limits))
        defaultAggregation = self.safe_string(options, 'defaultAggregation', '0')
        aggregations = self.safe_value(options, 'aggregations', [])
        aggregation = self.safe_string(params, 'aggregation', defaultAggregation)
        if not self.in_array(aggregation, aggregations):
            raise NotSupported(self.id + ' watchOrderBook() aggregation must be one of ' + ', '.join(aggregations))
        params = self.omit(params, 'aggregation')
        subscribe = {
            'method': 'depth.subscribe',
            'id': self.request_id(),
            'params': [
                market['id'],
                limit,
                aggregation,
                True,
            ],
        }
        request = self.deep_extend(subscribe, params)
        orderbook = await self.watch(url, messageHash, request, messageHash)
        return orderbook.limit()

    async def watch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        """
        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market
        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int|None since: timestamp in ms of the earliest candle to fetch
        :param int|None limit: the maximum amount of candles to fetch
        :param dict params: extra parameters specific to the coinex api endpoint
        :returns [[int]]: A list of candles ordered as timestamp, open, high, low, close, volume
        """
        await self.load_markets()
        market = self.market(symbol)
        symbol = market['symbol']
        messageHash = 'ohlcv'
        type = None
        type, params = self.handle_market_type_and_params('watchOHLCV', market, params)
        if type != 'swap':
            raise NotSupported(self.id + ' watchOHLCV() is only supported for swap markets')
        url = self.urls['api']['ws'][type]
        subscribe = {
            'method': 'kline.subscribe',
            'id': self.request_id(),
            'params': [
                market['id'],
                self.safe_integer(self.timeframes, timeframe, timeframe),
            ],
        }
        request = self.deep_extend(subscribe, params)
        ohlcvs = await self.watch(url, messageHash, request, messageHash)
        if self.newUpdates:
            limit = ohlcvs.getLimit(symbol, limit)
        return self.filter_by_since_limit(ohlcvs, since, limit, 0, True)

    def handle_delta(self, bookside, delta):
        bidAsk = self.parse_bid_ask(delta, 0, 1)
        bookside.storeArray(bidAsk)

    def handle_deltas(self, bookside, deltas):
        for i in range(0, len(deltas)):
            self.handle_delta(bookside, deltas[i])

    def handle_order_book(self, client, message):
        #
        #     {
        #         "method": "depth.update",
        #         "params": [
        #             False,
        #             {
        #                 "asks": [
        #                     ["46350.52", "1.07871851"],
        #                     ...
        #                 ],
        #                 "bids": [
        #                     ["46349.61", "0.04000000"],
        #                     ...
        #                 ],
        #                 "last": "46349.93",
        #                 "time": 1639987469166,
        #                 "checksum": 1533284725
        #             },
        #             "BTCUSDT"
        #         ],
        #         "id": null
        #     }
        #
        params = self.safe_value(message, 'params', [])
        fullOrderBook = self.safe_value(params, 0)
        orderBook = self.safe_value(params, 1)
        marketId = self.safe_string(params, 2)
        market = self.safe_market(marketId)
        symbol = market['symbol']
        name = 'orderbook'
        messageHash = name + ':' + symbol
        timestamp = self.safe_number(orderBook, 'time')
        currentOrderBook = self.safe_value(self.orderbooks, symbol)
        if fullOrderBook:
            snapshot = self.parse_order_book(orderBook, symbol, timestamp)
            if currentOrderBook is None:
                orderBook = self.order_book(snapshot)
                self.orderbooks[symbol] = orderBook
            else:
                orderBook = self.orderbooks[symbol]
                orderBook.reset(snapshot)
        else:
            asks = self.safe_value(orderBook, 'asks', [])
            bids = self.safe_value(orderBook, 'bids', [])
            self.handle_deltas(currentOrderBook['asks'], asks)
            self.handle_deltas(currentOrderBook['bids'], bids)
            currentOrderBook['nonce'] = timestamp
            currentOrderBook['timestamp'] = timestamp
            currentOrderBook['datetime'] = self.iso8601(timestamp)
            self.orderbooks[symbol] = currentOrderBook
        # self.check_order_book_checksum(self.orderbooks[symbol])
        client.resolve(self.orderbooks[symbol], messageHash)

    def check_order_book_checksum(self, orderBook):
        asks = self.safe_value(orderBook, 'asks', [])
        bids = self.safe_value(orderBook, 'bids', [])
        string = ''
        bidsLength = len(bids)
        for i in range(0, bidsLength):
            bid = bids[i]
            if i != 0:
                string += ':'
            string += bid[0] + ':' + bid[1]
        asksLength = len(asks)
        for i in range(0, asksLength):
            ask = asks[i]
            if bidsLength != 0:
                string += ':'
            string += ask[0] + ':' + ask[1]
        signedString = self.hash(string, 'cr32', 'hex')
        checksum = self.safe_string(orderBook, 'checksum')
        if checksum != signedString:
            raise ExchangeError(self.id + ' watchOrderBook() checksum failed')

    async def watch_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        await self.authenticate(params)
        messageHash = 'orders'
        market = None
        type, query = self.handle_market_type_and_params('watchOrders', market, params)
        message = {
            'method': 'order.subscribe',
            'id': self.request_id(),
        }
        if symbol is not None:
            market = self.market(symbol)
            symbol = market['symbol']
            message['params'] = [market['id']]
            messageHash += ':' + symbol
        else:
            message['params'] = self.ids
        url = self.urls['api']['ws'][type]
        request = self.deep_extend(message, query)
        orders = await self.watch(url, messageHash, request, messageHash, request)
        if self.newUpdates:
            limit = orders.getLimit(symbol, limit)
        return self.filter_by_symbol_since_limit(orders, symbol, since, limit, True)

    def handle_orders(self, client, message):
        #
        #  spot
        #
        #      {
        #          method: 'order.update',
        #          params: [
        #              1,
        #              {
        #                  id: 77782469357,
        #                  type: 1,
        #                  side: 2,
        #                  user: 1849116,
        #                  account: 0,
        #                  option: 2,
        #                  ctime: 1653961043.048967,
        #                  mtime: 1653961043.048967,
        #                  market: 'BTCUSDT',
        #                  source: 'web',
        #                  client_id: '',
        #                  price: '1.00',
        #                  amount: '1.00000000',
        #                  taker_fee: '0.0020',
        #                  maker_fee: '0.0020',
        #                  left: '1.00000000',
        #                  deal_stock: '0',
        #                  deal_money: '0',
        #                  money_fee: '0',
        #                  stock_fee: '0',
        #                  asset_fee: '0',
        #                  fee_discount: '1',
        #                  last_deal_amount: '0',
        #                  last_deal_price: '0',
        #                  last_deal_time: 0,
        #                  last_deal_id: 0,
        #                  last_role: 0,
        #                  fee_asset: null,
        #                  stop_id: 0
        #              }
        #          ],
        #          id: null
        #      }
        #
        #  swap
        #
        #      {
        #          method: 'order.update',
        #          params: [
        #              1,
        #              {
        #                  order_id: 23423462821,
        #                  position_id: 0,
        #                  stop_id: 0,
        #                  market: 'BTCUSDT',
        #                  type: 1,
        #                  side: 2,
        #                  target: 0,
        #                  effect_type: 1,
        #                  user_id: 1849116,
        #                  create_time: 1653961509.25049,
        #                  update_time: 1653961509.25049,
        #                  source: 'web',
        #                  price: '1.00',
        #                  amount: '1.0000',
        #                  taker_fee: '0.00050',
        #                  maker_fee: '0.00030',
        #                  left: '1.0000',
        #                  deal_stock: '0.00000000000000000000',
        #                  deal_fee: '0.00000000000000000000',
        #                  deal_profit: '0.00000000000000000000',
        #                  last_deal_amount: '0.00000000000000000000',
        #                  last_deal_price: '0.00000000000000000000',
        #                  last_deal_time: 0,
        #                  last_deal_id: 0,
        #                  last_deal_type: 0,
        #                  last_deal_role: 0,
        #                  client_id: '',
        #                  fee_asset: '',
        #                  fee_discount: '0.00000000000000000000',
        #                  deal_asset_fee: '0.00000000000000000000',
        #                  leverage: '3',
        #                  position_type: 2
        #              }
        #          ],
        #          id: null
        #      }
        #
        params = self.safe_value(message, 'params', [])
        order = self.safe_value(params, 1, {})
        parsedOrder = self.parse_ws_order(order)
        if self.orders is None:
            limit = self.safe_integer(self.options, 'ordersLimit', 1000)
            self.orders = ArrayCacheBySymbolById(limit)
        self.orders.append(parsedOrder)
        messageHash = 'orders'
        client.resolve(self.orders, messageHash)
        messageHash += ':' + parsedOrder['symbol']
        client.resolve(self.orders, messageHash)

    def parse_ws_order(self, order):
        #
        #  spot
        #
        #       {
        #           id: 77782469357,
        #           type: 1,
        #           side: 2,
        #           user: 1849116,
        #           account: 0,
        #           option: 2,
        #           ctime: 1653961043.048967,
        #           mtime: 1653961043.048967,
        #           market: 'BTCUSDT',
        #           source: 'web',
        #           client_id: '',
        #           price: '1.00',
        #           amount: '1.00000000',
        #           taker_fee: '0.0020',
        #           maker_fee: '0.0020',
        #           left: '1.00000000',
        #           deal_stock: '0',
        #           deal_money: '0',
        #           money_fee: '0',
        #           stock_fee: '0',
        #           asset_fee: '0',
        #           fee_discount: '1',
        #           last_deal_amount: '0',
        #           last_deal_price: '0',
        #           last_deal_time: 0,
        #           last_deal_id: 0,
        #           last_role: 0,
        #           fee_asset: null,
        #           stop_id: 0
        #       }
        #
        #  swap
        #
        #      {
        #          order_id: 23423462821,
        #          position_id: 0,
        #          stop_id: 0,
        #          market: 'BTCUSDT',
        #          type: 1,
        #          side: 2,
        #          target: 0,
        #          effect_type: 1,
        #          user_id: 1849116,
        #          create_time: 1653961509.25049,
        #          update_time: 1653961509.25049,
        #          source: 'web',
        #          price: '1.00',
        #          amount: '1.0000',
        #          taker_fee: '0.00050',
        #          maker_fee: '0.00030',
        #          left: '1.0000',
        #          deal_stock: '0.00000000000000000000',
        #          deal_fee: '0.00000000000000000000',
        #          deal_profit: '0.00000000000000000000',
        #          last_deal_amount: '0.00000000000000000000',
        #          last_deal_price: '0.00000000000000000000',
        #          last_deal_time: 0,
        #          last_deal_id: 0,
        #          last_deal_type: 0,
        #          last_deal_role: 0,
        #          client_id: '',
        #          fee_asset: '',
        #          fee_discount: '0.00000000000000000000',
        #          deal_asset_fee: '0.00000000000000000000',
        #          leverage: '3',
        #          position_type: 2
        #      }
        #
        #  order.update_stop
        #
        #       {
        #           id: 78006745870,
        #           type: 1,
        #           side: 2,
        #           user: 1849116,
        #           account: 1,
        #           option: 70,
        #           direction: 1,
        #           ctime: 1654171725.131976,
        #           mtime: 1654171725.131976,
        #           market: 'BTCUSDT',
        #           source: 'web',
        #           client_id: '',
        #           stop_price: '1.00',
        #           price: '1.00',
        #           amount: '1.00000000',
        #           taker_fee: '0.0020',
        #           maker_fee: '0.0020',
        #           fee_discount: '1',
        #           fee_asset: null,
        #           status: 0
        #       }
        #
        timestamp = self.safe_timestamp_2(order, 'update_time', 'mtime')
        marketId = self.safe_string(order, 'market')
        typeCode = self.safe_string(order, 'type')
        type = self.safe_string({
            '1': 'limit',
            '2': 'market',
        }, typeCode)
        sideCode = self.safe_string(order, 'side')
        side = self.safe_string({
            '1': 'sell',
            '2': 'buy',
        }, sideCode)
        remaining = self.safe_string(order, 'left')
        amount = self.safe_string(order, 'amount')
        status = self.safe_string(order, 'status')
        market = self.safe_market(marketId)
        cost = self.safe_string(order, 'deal_money')
        filled = self.safe_string(order, 'deal_stock')
        average = None
        if market['swap']:
            leverage = self.safe_string(order, 'leverage')
            cost = Precise.string_div(filled, leverage)
            average = Precise.string_div(filled, amount)
            filled = None
        fee = None
        feeCost = self.omit_zero(self.safe_string(order, 'money_fee'))
        if feeCost is not None:
            feeCurrencyId = self.safe_string(order, 'fee_asset', market['quote'])
            fee = {
                'currency': self.safe_currency_code(feeCurrencyId),
                'cost': feeCost,
            }
        return self.safe_order({
            'info': order,
            'id': self.safe_string_2(order, 'order_id', 'id'),
            'clientOrderId': self.safe_string(order, 'client_id'),
            'datetime': self.iso8601(timestamp),
            'timestamp': timestamp,
            'lastTradeTimestamp': self.safe_timestamp(order, 'last_deal_time'),
            'symbol': market['symbol'],
            'type': type == 'limit' if 1 else 'market',
            'timeInForce': None,
            'postOnly': None,
            'side': side,
            'price': self.safe_string(order, 'price'),
            'stopPrice': self.safe_string(order, 'stop_price'),
            'triggerPrice': self.safe_string(order, 'stop_price'),
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'cost': cost,
            'average': average,
            'status': self.parse_ws_order_status(status),
            'fee': fee,
            'trades': None,
        }, market)

    def parse_ws_order_status(self, status):
        statuses = {
            '0': 'pending',
            '1': 'ok',
        }
        return self.safe_string(statuses, status, status)

    def handle_message(self, client, message):
        error = self.safe_value(message, 'error')
        if error is not None:
            raise ExchangeError(self.id + ' ' + self.json(error))
        method = self.safe_string(message, 'method')
        handlers = {
            'state.update': self.handle_ticker,
            'asset.update': self.handle_balance,
            'deals.update': self.handle_trades,
            'depth.update': self.handle_order_book,
            'order.update': self.handle_orders,
            'kline.update': self.handle_ohlcv,
            'order.update_stop': self.handle_orders,
        }
        handler = self.safe_value(handlers, method)
        if handler is not None:
            return handler(client, message)
        return self.handle_subscription_status(client, message)

    def handle_authentication_message(self, client, message):
        #
        #     {
        #         error: null,
        #         result: {
        #             status: 'success'
        #         },
        #         id: 1
        #     }
        #
        future = self.safe_value(client.futures, 'authenticated')
        if future is not None:
            future.resolve(True)
        return message

    def handle_subscription_status(self, client, message):
        id = self.safe_string(message, 'id')
        subscription = self.safe_value(client.subscriptions, id)
        if subscription is not None:
            futureIndex = self.safe_string(subscription, 'future')
            future = self.safe_value(client.futures, futureIndex)
            if future is not None:
                future.resolve(True)
            del client.subscriptions[id]

    def authenticate(self, params={}):
        type = None
        type, params = self.handle_market_type_and_params('authenticate', None, params)
        url = self.urls['api']['ws'][type]
        client = self.client(url)
        time = self.milliseconds()
        if type == 'spot':
            messageHash = 'authenticated:spot'
            authenticated = self.safe_value(client.futures, messageHash)
            if authenticated is not None:
                return
            future = client.future(messageHash)
            requestId = self.request_id()
            subscribe = {
                'id': requestId,
                'future': 'authenticated:spot',
            }
            signData = 'access_id=' + self.apiKey + '&tonce=' + self.number_to_string(time) + '&secret_key=' + self.secret
            hash = self.hash(self.encode(signData), 'md5')
            request = {
                'method': 'server.sign',
                'params': [
                    self.apiKey,
                    hash.upper(),
                    time,
                ],
                'id': requestId,
            }
            self.spawn(self.watch, url, messageHash, request, requestId, subscribe)
            return future
        else:
            messageHash = 'authenticated:swap'
            authenticated = self.safe_value(client.futures, messageHash)
            if authenticated is not None:
                return
            future = client.future('authenticated:swap')
            requestId = self.request_id()
            subscribe = {
                'id': requestId,
                'future': 'authenticated:swap',
            }
            signData = 'access_id=' + self.apiKey + '&timestamp=' + self.number_to_string(time) + '&secret_key=' + self.secret
            hash = self.hash(self.encode(signData), 'sha256', 'hex')
            request = {
                'method': 'server.sign',
                'params': [
                    self.apiKey,
                    hash.lower(),
                    time,
                ],
                'id': requestId,
            }
            self.spawn(self.watch, url, messageHash, request, requestId, subscribe)
            return future
