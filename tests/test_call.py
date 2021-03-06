import unittest
import nationstates as ns
from random import choice
import datetime
USERAGENT = "Automated Testing Builds by Travis CL for the nationstates API wrapper by The United Island Tribes. dolphdevgithub@gmail.com"

import os
test_nation = 'Python Nationstates API wrapper'
test_nation_r = 'pynationstates_telegram_recipient'
PASSWORD = os.environ.get('password')
tgid = os.environ.get('telegram_tgid')
key = os.environ.get('telegram_key')
client_key = os.environ.get('telegram_clientkey')
del os

sep_api =  ns.Nationstates(USERAGENT)

joint_api = ns.Nationstates(USERAGENT)
test_nation_nonauth = joint_api.nation(test_nation)
test_auth_nation = joint_api.nation(test_nation, password=PASSWORD)
test_nation_r = joint_api.nation(test_nation_r)


def grab_id(newfactbookresponse_text):
    part1 = newfactbookresponse_text.split('id=')
    return part1[1].split('">')[0]


class SetupCallTest(unittest.TestCase):

    def test_create_ns(self):
        try:
            api = ns.Nationstates(USERAGENT)
        except Exception as Err:
            self.fail(Err)

class SeperateCallTest(unittest.TestCase):

    def test_nation_call(self):
        try:
            api = sep_api
            mycall = api.nation("testlandia")
            mycall.get_shards(choice(mycall.auto_shards))
            mycall.get_shards(choice(mycall.auto_shards), full_response=True)

        except Exception as Err:
            self.fail(Err)

    def test_region_call(self):
        try:
            api = sep_api

            mycall = api.region("Balder")
            mycall.get_shards(choice(mycall.auto_shards))
            mycall.get_shards(choice(mycall.auto_shards), full_response=True)

        except Exception as Err:
            self.fail(Err)

    def test_world_call(self):
        try:
            api = sep_api

            mycall = api.world()
            mycall.get_shards(choice(mycall.auto_shards))
            mycall.get_shards(choice(mycall.auto_shards), full_response=True)
        except Exception as Err:
            self.fail(Err)


    def test_wa_call(self):
        try:
            api = sep_api

            mycall = api.wa("1")
            mycall.get_shards(choice(mycall.auto_shards))
            mycall.get_shards(choice(mycall.auto_shards), full_response=True)
        except Exception as Err:
            self.fail(Err)

    def test_cards_indv_call(self):
        try:
            api = sep_api

            mycall = api.cards()
            mycall.individual_cards(1, 1)
            mycall.individual_cards(1, 1, full_response=True)
            mycall.individual_cards(1, 1, 'trades')
            mycall.individual_cards(1, 1, ns.Shard('trades'))
            mycall.individual_cards(1, 1, (ns.Shard('trades'),))

            # mycall.get_shards(choice(mycall.auto_shards))
            # mycall.get_shards(choice(mycall.auto_shards), full_response=True)
        except Exception as Err:
            raise Err
            self.fail(Err)

    def test_cards_decks_call(self):
        try:
            api = sep_api

            mycall = api.cards()
            mycall.decks(nation_name='testlandia')
            mycall.decks(nation_name='testlandia', full_response=True)
            mycall.decks(nation_id=1)

            # mycall.get_shards(choice(mycall.auto_shards))
            # mycall.get_shards(choice(mycall.auto_shards), full_response=True)
        except Exception as Err:
            self.fail(Err)

    def test_cards_decksinfo_call(self):
        try:
            api = sep_api

            mycall = api.cards()
            mycall.deck_owner_info(nation_name='testlandia')
            mycall.deck_owner_info(nation_name='testlandia', full_response=True)
            mycall.deck_owner_info(nation_id=1)

            # mycall.get_shards(choice(mycall.auto_shards))
            # mycall.get_shards(choice(mycall.auto_shards), full_response=True)
        except Exception as Err:
            self.fail(Err)

    def test_cards_asks_and_bids_call(self):
        try:
            api = sep_api

            mycall = api.cards()
            mycall.asks_and_bids(nation_name='testlandia')
            mycall.asks_and_bids(nation_name='testlandia', full_response=True)
            mycall.asks_and_bids(nation_id=1)

            # mycall.get_shards(choice(mycall.auto_shards))
            # mycall.get_shards(choice(mycall.auto_shards), full_response=True)
        except Exception as Err:
            self.fail(Err)

    def test_cards_collections_call(self):
        try:
            api = sep_api

            mycall = api.cards()
            mycall.collections(nation_name='testlandia')
            mycall.collections(nation_name='testlandia', full_response=True)
            mycall.collections(nation_id=1)

            # mycall.get_shards(choice(mycall.auto_shards))
            # mycall.get_shards(choice(mycall.auto_shards), full_response=True)
        except Exception as Err:
            self.fail(Err)


    def test_cards_auctions_call(self):
        try:
            api = sep_api

            mycall = api.cards()
            mycall.auctions()
            mycall.auctions(full_response=True)

            # mycall.get_shards(choice(mycall.auto_shards))
            # mycall.get_shards(choice(mycall.auto_shards), full_response=True)
        except Exception as Err:
            self.fail(Err)



    def test_cards_trades_call(self):
        try:
            api = sep_api

            mycall = api.cards()
            mycall.trades()
            mycall.trades(full_response=True)
            mycall.collections(nation_id=1)

            # mycall.get_shards(choice(mycall.auto_shards))
            # mycall.get_shards(choice(mycall.auto_shards), full_response=True)
        except Exception as Err:
            self.fail(Err)

    def test_auto_shard_static_n(self):
        try:
            api = sep_api

            mycall = api.nation("testlandia")
            mycall.fullname
        except Exception as Err:
            self.fail(Err)

    def test_auto_shard_static_r(self):
        try:
            api = sep_api

            mycall = api.region("balder")
            mycall.numnations
        except Exception as Err:
            self.fail(Err)

    def test_auto_shard_static_w(self):
        try:
            api = sep_api

            mycall = api.world()
            mycall.numnations
        except Exception as Err:
            self.fail(Err)

    def test_auto_shard_static_wa(self):
        try:
            api = sep_api

            mycall = api.wa("1")
            mycall.numnations
        except Exception as Err:
            self.fail(Err)

class ApiJoinTest(unittest.TestCase):

    def test_private_nation(self):
        try:
            test_auth_nation.get_shards('ping')
        except Exception as Err:
            self.fail(Err)


    def test_create_dispatch(self):
        from datetime import datetime
        now = datetime.now
        try:
            resp = test_auth_nation.create_dispatch(title='AUTOMATED ADD DISPATCH TEST', text=str(now()), category=1, subcategory=105, full_response=True)
            dispatch_id = grab_id(resp['data']['nation']['success'])
            resp = test_auth_nation.remove_dispatch(dispatch_id=dispatch_id, full_response=True)

            resp = test_auth_nation.create_dispatch(title='AUTOMATED ADD DISPATCH TEST', text=str(now()), category=1, subcategory=105, full_response=False)
            dispatch_id = grab_id(resp.success)
            resp = test_auth_nation.remove_dispatch(dispatch_id=dispatch_id, full_response=True)


        except Exception as Err:
            self.fail(Err)

    def test_edit_dispatch(self):
        from datetime import datetime
        now = datetime.now
        try:
            resp = test_auth_nation.create_dispatch(title='AUTOMATED ADD DISPATCH EDIT TEST', text=str(now()), category=1, subcategory=105, full_response=False)
            dispatch_id = grab_id(resp.success)
            resp = test_auth_nation.edit_dispatch(dispatch_id=dispatch_id, title='EDIT TEST', text="THIS POST WAS LAST EDITED AT:" + str(now()), category=1, subcategory=111, full_response=False)
            resp = test_auth_nation.remove_dispatch(dispatch_id=dispatch_id, full_response=True)           
            resp = test_auth_nation.create_dispatch(title='AUTOMATED ADD DISPATCH EDIT TEST', text=str(now()), category=1, subcategory=105, full_response=False)            
            dispatch_id = grab_id(resp.success)            
            resp = test_auth_nation.edit_dispatch(dispatch_id=dispatch_id, title='EDIT TEST', text="THIS POST WAS LAST EDITED AT:" + str(now()), category=1, subcategory=111, full_response=True)
            resp = test_auth_nation.remove_dispatch(dispatch_id=dispatch_id, full_response=True)
        
        except Exception as Err:
            self.fail(Err)

    def test_remove_dispatch(self):
        from datetime import datetime
        now = datetime.now
        try:
            resp = test_auth_nation.create_dispatch(title='AUTOMATED ADD DISPATCH REMOVE TEST', text=str(now()), category=1, subcategory=105, full_response=False)
            dispatch_id = grab_id(resp.success)
            resp = test_auth_nation.remove_dispatch(dispatch_id=dispatch_id)
            resp = test_auth_nation.create_dispatch(title='AUTOMATED ADD DISPATCH REMOVE TEST', text=str(now()), category=1, subcategory=105, full_response=False)
            dispatch_id = grab_id(resp.success)
            resp = test_auth_nation.remove_dispatch(dispatch_id=dispatch_id, full_response=True)
        except Exception as Err:
            self.fail(Err)


    def test_telegram_send(self):
        from datetime import datetime
        import time
        now = datetime.now
        try:
            telegram = joint_api.telegram(tgid=tgid, key=key, client_key=client_key)
            test_nation_r.send_telegram(telegram)
            try:
                test_nation_r.send_telegram(telegram)
                self.fail('API was suppose to block this')
            except ns.nsapiwrapper.exceptions.APIRateLimitBan:
                pass
            try:
                telegram.send_telegram(test_nation_r.name)
            except ns.nsapiwrapper.exceptions.APIRateLimitBan:
                # Just testing code path works - to much wasted time to wait 30 seconds
                pass
        except Exception as Err:
            raise (Err)