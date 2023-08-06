## Asklora module for ingestion data
### drop support for RKD for this version

### .env config
`BROKER_API_URL=brokerurl`

`MARKET_API_URL=market url`

`BROKER_KEY=key`

`BROKER_SECRET=secret`

- usage
```python
import asklora

portal = asklora.Portal()

rest = portal.get_broker_client() # get a REST client for trade, user, position , order
marketrest = portal.get_market_client() # get a REST client for market data
eventclient = portal.get_event_client() # get an event client for trade, user, position, order
```