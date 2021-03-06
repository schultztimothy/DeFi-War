from defiwar.dex.aave import Aave
from defiwar.dex.bancor import Bancor
from defiwar.dex.compound import Compound
from defiwar.dex.curve_fi import CurveFi
from defiwar.dex.dydx import DyDx
from defiwar.dex.idle_fi import IdleFi
from defiwar.dex.oasis import Oasis
from defiwar.dex.one_inch import OneInch
from defiwar.dex.radar_relay import RadarRelay
from defiwar.dex.synthetix import Synthetix
from defiwar.dex.kyber import Kyber
from defiwar.dex.uniswap import Uniswap
from defiwar.dex.zero_x import ZeroX

from web3 import HTTPProvider
from defiwar.dex.common import *

if __name__ == "__main__":

    web3 = Web3(HTTPProvider('Your Infura endpoint'))
    aave_dex = Aave()
    bancor_dex = Bancor()
    compound_dex = Compound()
    curve_fi_dex = CurveFi(web3)
    dydx_dex = DyDx()
    idle_dex = IdleFi(web3)
    oasis_dex = Oasis()
    one_inch_dex = OneInch(web3)
    radar_relay_dex = RadarRelay()
    synthetix_dex = Synthetix()
    kyber_dex = Kyber()
    uniswap_dex = Uniswap(web3)
    zero_x_dex = ZeroX()

    # Compound API Calls
    '''print(compound_dex.get_account('addresses[]=0x4B3897e40749587FFBfB2732008d026DB2C8D588', 'block_number=0'))
    print(compound_dex.get_ctoken('addresses[]=0x4B3897e40749587FFBfB2732008d026DB2C8D588'))
    print(compound_dex.get_graph('asset=0xf5dce57282a584d2746faf1593d3121fcac444dc'))
    print(compound_dex.get_gov_proposals())
    print(compound_dex.get_gov_proposal_vote_receipts('proposal_id=2'))
    print(compound_dex.get_gov_accounts('page_size=1'))
    print(compound_dex.get_gov_history())

    # One1inch API Calls
    print(one_inch_dex.get_quote('100', from_token_symbol='DAI', to_token_symbol='ETH'))
    print(one_inch_dex.get_tokens())
    print(one_inch_dex.get_exchanges())

    # Radar Relay API Calls
    print(radar_relay_dex.list_markets())
    print(radar_relay_dex.get_market('marketId=ZRX-WETH'))
    print(radar_relay_dex.get_market_ticker('ZRX-WETH'))
    print(radar_relay_dex.get_market_stats('ZRX-WETH'))
    print(radar_relay_dex.get_market_history('ZRX-WETH'))'''

    # ZeroX API Calls
    # print(zero_x_dex.get_swap_tokens())

    # Aave GraphQl API
    print(aave_dex.graph_request('swaps'))
    print(aave_dex.graph_request('repays'))
    print(aave_dex.graph_request('flashLoans'))

    # DyDx API
    # print(dydx_dex.get_markets())
    # print(one_inch_dex.get_expected_return(dai_token, usdc_token, 100, 100, 0))
    # print(uniswap_dex.get_eth_balance(uni_bat_token))
    # print(uniswap_dex.get_token_balance(bat_token, uni_bat_token))

    # Kyber API
    print(kyber_dex.get_buy_rate(
        'id=0xdd974D5C2e2928deA5F71b9825b8b646686BD200',
        'qty=300',
        'id=0xd26114cd6EE289AccF82350c8d8487fedB8A0C07',
        'qty=10.1'
    ))
    # print(kyber_dex.get_change24h(only_official_reserve=False))
    # print(kyber_dex.get_currencies())
    # print(kyber_dex.get_gas_limit_config())
    # print(kyber_dex.get_market())
    print(kyber_dex.get_quote_amount(
        'base=0xdd974d5c2e2928dea5f71b9825b8b646686bd200',
        'quote=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
        'base_amount=10', 'type=sell'
    ))
    print(kyber_dex.get_gas_limit(
        'source=0x6b175474e89094c44da98b954eedeac495271d0f',
        'dest=0xd26114cd6ee289accf82350c8d8487fedb8a0c07',
        'amount=10000'
    ))
    # print(kyber_dex.get_users_currencies('0x8fA07F46353A2B17E92645592a94a0Fc1CEb783F'))

    # Oasis API
    # print(oasis_dex.get_markets('eth', 'dai'))
    # print(oasis_dex.get_prices('eth', 'dai'))
    # print(oasis_dex.get_volumes('eth', 'dai'))
    # print(oasis_dex.get_orders())
    # print(oasis_dex.get_trades('eth', 'dai', 'limit=2'))
    # print(oasis_dex.get_pairs('eth', 'dai'))

    # Bancor API
    # print(bancor_dex.get_historical_volume(to_currency_code='BNT', from_currency_code='ETH', time_frame='week'))
    # print(bancor_dex.get_price_ticker(to_token='BNT', from_token='ETH', display_currency='ETH'))
    # print(bancor_dex.get_available_pairs())

    # Curve API
    # print(curve_fi_dex.a('compound'))
    # print(curve_fi_dex.total_supply('compound'))
    # print(curve_fi_dex.get_virtual_price('compound'))
    # print(curve_fi_dex.coins('compound', 1))
    # print(curve_fi_dex.balances('compound', 1))
    # print(curve_fi_dex.future_fee('compound'))
    # print(curve_fi_dex.future_owner('compound'))
    # print(curve_fi_dex.name('compound'))
    # print(curve_fi_dex.symbol('compound'))
    # print(curve_fi_dex.decimals('compound'))

    # Synthetix API
    # print(synthetix_dex.graph_request('snxholders', ['id', 'balanceOf', 'collateral', 'transferable']))
    # print(synthetix_dex.graph_request('synthetixes'))
    # print(synthetix_dex.graph_request('transfers'))
    # print(synthetix_dex.graph_request('issueds'))
    # print(synthetix_dex.graph_request('issuers'))
    # print(synthetix_dex.graph_request('burneds'))
    # print(synthetix_dex.graph_request('contractUpdateds'))
    # print(synthetix_dex.graph_request('rewardEscrowHolders'))
    # print(synthetix_dex.graph_request('feesClaimeds'))

    # Idle Finance API
    print(idle_dex.get_aprs('dai', 'max'))
    print(idle_dex.total_supply('usdt', 'risk'))
    print(idle_dex.total_supply('usdc', 'max'))
    print(idle_dex.all_available_tokens('dai', 'max', 1))
