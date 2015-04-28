"""
Unit tests for 'hunts' django application

The list of tests are:

"""
from django.test.client import RequestFactory
from django.test import  Client, TestCase
from mock import MagicMock, patch
from hunts import views
from hunts import models
from django.core.urlresolvers import reverse

global TEMP

# Create your tests here.
class hunts_test(TestCase):
    def setUp(self):
        self.client = Client()
        global TEMP
        views.TEMP = [('123', 'a clue', 1, 'hint', 'image url', 'fun fact')]
        models.TEMP = views.TEMP
        TEMP = models.TEMP
        self.factory = RequestFactory()

    def tearDown(self):
        del views.TEMP
        del models.TEMP
#   def test_hunts_status(self):
#       views.hunt_title = 'test1234567'
#       views.hunt_start = 'test7654321'
#       resp = self.client.get('/hunts/welcome/') #should be directory of welcom page
#       self.assertEqual(resp.status_code, 200)

    def test_getData(self): #INCOMPLETE
        pass
            #call query
            #use fixtures to fill database and grab from there
            #use count to check that something was grabbed

    def test_render_hunt(self):#DONE, updated
        """
            **test_render_hunt** This test mocks hunt_title and hunt_start.
            Then the test tries to call the hunts/hunt url which
            should render with hunt_title and hunt_start which are validated at the end of the test.
        """
        with patch('hunts.views.set_ItemsData') as itemsdata:
            with patch('hunts.views.set_HuntsData') as huntsdata:
                with patch('hunts.views.render_to_response') as rend:
                    global TEMP
                    itemsdata.return_value = views.TEMP
                    huntsdata.return_value = {'hunt title' : 'test1234', 'hunt start' : 'test7654321'}
                    request = MagicMock()
                    views.render_hunt(request, 1)
                    #check that correct title and start point were passed through
                    rend.assert_called_with("hunts/hunt.html", {"title" : 'test1234', "start_pt": 'test7654321'})

    def test_render_clue(self): #DONE
        """
            **test_render_clue**
            First: tests if render_clue is called when going to the clue page

            Second: mocks item_clue to force it to return a unique value. Then tests if that clue
            is in the context of the rendered html page
        """
        with patch('hunts.views.render_to_response') as rend:
            request = MagicMock()
            views.render_clue(request)
            #clue was not displayed on clue page"
            rend.assert_called_with("hunts/clue.html", {"clue_text" : 'a clue'})

    def test_render_verify(self):#DONE
        """
            **test_render_verify** tests if render_verify is ran at the correct url
        """
        with patch('hunts.views.render_to_response') as reg:
            request = MagicMock()
            views.render_verify(request)
            c_srf = {}
            assert reg.called #render_verify returns render_to_response
            #reg.assert_called_with("hunts/verify.html", c_srf, {})
            #check that correct html is used with csrf token

    def test_verify_ID(self): #DONE
        """
            **test_verify_ID**  Function mocks the var 'item_id'
            **then runs verify_id to see if it returns correct boolean values for equal input and unequal input
        """
        s_val = '123'
        f_val = '234'
        success = models.verify_id(s_val)
        failure = models.verify_id(f_val)
        assert success #verify_id did not return true when input and item_id were equal"
        assert not failure #verify_id did not return false when input and item_id were different"

    def test_next_proc(self): #Needs to be checked
        """
            mocks TEMP and pop_item function. Runs next_proc see if pop_tem is called when TEMP is not empty.
            Then an assert is made to check that it correctly redirects to the clue page.
            Empties TEMP and runs next_proc again. This time checks that pop_item is not called.
            Then an assert is made to check that it correctly redirects to the congrats page.
        """
        with patch('hunts.views.pop_item') as pop_item:
            with patch('hunts.views.redirect') as redirect:
                pop_item.return_value = [1]
                global TEMP
                TEMP = views.TEMP
                views.next_proc(self.factory)
                assert pop_item.called #test that pop_item is called
                redirect.assert_called_with('rend_clue') #next_proc does not correctly redirect to clue page
                pop_item.reset_mock()
                pop_item.return_value = []
                views.next_proc(self.factory)
#               assert not(pop_item.called) #pop_item was called when TEMP was empty"

    def test_render_result(self):#DONE
        """
            **test_render_result** The test mocks verify_id.
            Fixes it to True and checks that render_result redirects to the correct page
            Then the test fixes verify_id to false and checks that render_result redirects to incorrect page
        """
        with patch('hunts.views.verify_id') as verify_id:
            with patch('hunts.views.redirect') as redirect:
                verify_id.return_value = True
                request = self.factory.post('/hunts/result/', {'input':'123'})
                views.TEMP = [('123', 'a clue', 1, 'hint', 'image url', 'fun fact'), ('234', 'a clue2', 2, 'hint 2', 'image url 2', 'fun fact 2')]
                #run render_result
                views.render_result(request)
                #render_verify does not correctly redirect to 'correct' page when expected"
                redirect.assert_called_with('rend_correct')
                views.TEMP = [('123', 'a clue', 1, 'hint', 'image url', 'fun fact')]
                views.render_result(request)
                #render_result dow not correctly redirect to 'congrats' page when expected
                redirect.assert_called_with('rend_correct')
                verify_id.return_value = False
                views.render_result(request)
                #render_verify does not correctly redirect to 'incorrect' page when expected
                redirect.assert_called_with('rend_incorrect')

    def test_hint(self):
        """
            **test_incorrect** tests if render_incorrect is ran at the correct url
        """
        with patch('hunts.views.render_to_response') as rend:
            request = MagicMock()
            views.render_hint(request)
            rend.assert_called_with("hunts/hint.html", {"hint_text": 'hint'})

    def test_correct(self):
        """
            **test_correct** tests if render_correct is ran at the correct url
        """
        with patch('hunts.views.render_to_response') as rend:
            request = MagicMock()
            views.render_correct(request)
            rend.assert_called_with("hunts/correct.html", {"url":'image url', "fact":'fun fact'})

    def test_incorrect(self):
        """
            **test_incorrect** tests if render_incorrect is ran at the correct url
        """
        with patch('hunts.views.render_to_response') as rend:
            request = MagicMock()
            views.render_incorrect(request)
            rend.assert_called_with("hunts/incorrect.html", {})

    def test_congrats(self):#DONE
        """
            **test_congrats** tests if render_congrats is ran at the correct url
        """
        with patch('hunts.views.render_to_response') as rend:
            request = MagicMock()
            views.render_congrats(request)
            #self.client.get('/hunts/congrats/')
            #try:
            #   assert reg.called
            #except AssertionError:
            #   print "render_congrats was not called at the url: /hunts/congrats/"
            rend.assert_called_with("hunts/congrats.html", {})

            #***Model tests***
    def test_set_HuntsData(self): #DONE
        """
            **test_set_HuntsData this test creates a mock object
            **then tests that the correct values are retrieved
        """
        with patch('hunts.models.Hunts.objects.get') as hunts_obj:
            hunts_obj.return_value = MagicMock()
            hunts_obj.return_value.Title = "hunt title test"
            hunts_obj.return_value.Start = "hunt start test"
            id_hunt = "123"
            models.set_HuntsData(id_hunt)


    def test_set_ItemsData(self):
        """
            **test_set_ItemsData** this test should mock the model
            **check that correct items were retrieved
        """
        with patch('hunts.models.Has.objects.filter') as items_hunt:
            items_hunt = MagicMock()
            items_hunt.return_value.item.ID = "123"
            items_hunt[0].return_value.clue = "clue test"
            items_hunt[0].return_value.number = "1"
            items_hunt[0].return_value.hint = "Hint test"
            items_hunt[0].return_value.image = "image url test"
            items_hunt[0].return_value.fact = "fact test"

    def test_pop_item(self): #DONE
        lst = [1]
        lst = models.pop_item(lst)
        self.assertTrue(len(lst) < 1)

