"""
Unit tests for 'cr_hunt' django application

The list of tests are:

"""
from django.test.client import RequestFactory
from django.test import  Client, TestCase
from django.contrib.auth.models import User
from mock import MagicMock, Mock, patch
from cr_hunt import views
from cr_hunt import models
from django.core.urlresolvers import reverse
# Create your tests here.
class hunts_test(TestCase):
    def setUp(self):
        views.hunt_id = '111222'
        views.i_counter = 0
        pass

    def tearDown(self):
        del views.hunt_id
        del views.i_counter
        pass

    def test_render_main(self):
        """
            **test_render_main** * Will test that correct url is called
        """
        with patch('cr_hunt.views.render_to_response') as rend:
            with patch('cr_hunt.views.redirect') as red:
                with patch('cr_hunt.views.gen_hunt_id') as genhid:
                    with patch('cr_hunt.views.get_cur_count') as getcount:
                        request = MagicMock()
                        request.user = MagicMock()
                        attrs = {'is_authenticated.return_value':True}
                        request.user.configure_mock(**attrs)
                        genhid.return_value = 'test1'
                        request.user.username = MagicMock()
                        request.user.username.return_value = 'user1'
                        getcount.return_value = 1
                        views.render_main(request)
                        assert rend.called # Check that rend got called
                        rend.assert_called_with("cr_hunt/cr_hunt_main.html") # Check that correct url is called
                        self.assertEqual(views.hunt_id, 'test1') #check that hunt_id got reassigned correctly
                        self.assertEqual(views.i_counter, 1) #check that i_counter is initialized to 0
                        attrs = {'is_authenticated.return_value':False}
                        request.user.configure_mock(**attrs)
                        views.render_main(request)
                        assert red.called
                        red.assert_called_with('cr_error')

    def test_render_ats(self):
        """
            **test_render_ats** * Will test that correct url is called with csrf token
        """
        with patch('cr_hunt.views.render_to_response') as rend:
            with patch('cr_hunt.views.redirect') as red:
                request = MagicMock()
                request.user = MagicMock()
                attrs = {'is_authenticated.return_value':True}
                request.user.configure_mock(**attrs)
                views.render_ats(request)
                c_srf = MagicMock()
                assert rend.called # Check that rend got called
                #rend.assert_called_with("cr_hunt/cr_hunt_title_strt.html", c_srf, {}) # check that rend got called with correct url and arguments
                attrs = {'is_authenticated.return_value':False}
                request.user.configure_mock(**attrs)
                views.render_ats(request)
                assert red.called
                red.assert_called_with('cr_error')

    def test_render_aitem(self):
        """
            **test_render_aitem** * Test that correct checks are performed and that form is generated and passed in as argument
        """
        with patch('cr_hunt.views.render_to_response') as rend:
            with patch('cr_hunt.views.ItemForm') as form_func:
                with patch('cr_hunt.views.redirect') as red:
                    request = MagicMock()
                    request.method = "POST"
                    attrs = {'is_authenticated.return_value':True}
                    request.user.configure_mock(**attrs)
                    form_func.is_valid.return_value = True
                    views.render_aitem(request)
                    assert rend.called
                    attrs = {'is_authenticated.return_value':False}
                    request.user.configure_mock(**attrs)
                    views.render_aitem(request)
                    assert red.called
                    red.assert_called_with('cr_error')
                    views.i_counter = 10
                    views.render_aitem(request)
                    red.assert_called_with('cr_end')

    def test_render_end(self):
        """
            **test_render_end** * Test that rend is called with correct url
        """
        with patch('cr_hunt.views.render_to_response') as rend:
            request = MagicMock()
            views.render_end(request)
            assert rend.called #check that rend is called
            rend.assert_called_with("cr_hunt/cr_hunt_end.html")

    def test_render_proc_ts(self):
        """
            **test_render_proc_ts** * Test that items are grabbed correctly
        """
        with patch('cr_hunt.views.add_hunt_its') as addf:
            with patch('cr_hunt.views.redirect') as red:
                request = MagicMock()
                request.method = "POST"
                def side_effect(*args):
                    def second_call(*args):
                        return 'test321'
                    request.POST.get.side_effect = second_call
                    return 'test123'
                request.POST.get = MagicMock(side_effect=side_effect)
                #request.POST.get('title', '').return_value = 'test123'
                #request.POST.get('start', '').return_value = 'test321'
                request.user = MagicMock()
                attrs = {'is_authenticated.return_value':True}
                request.user.configure_mock(**attrs)
                request.user.username = 'user1'
                views.render_proc_ts(request)
                assert addf.called
                addf.assert_called_with('111222', 'test123', 'test321', 'user1')
                assert red.called #test that redirect is called
                red.assert_called_with('cr_aitem')
                red.reset_mock()
                attrs = {'is_authenticated.return_value':False}
                request.user.configure_mock(**attrs)
                views.render_proc_ts(request)
                assert red.called
                red.assert_called_with('cr_error')

    def test_render_proc_it(self):
        """
            **test_render_proc_it** * Test that items are grabbed correctly
        """
        with patch('cr_hunt.views.redirect') as red:
            with patch('cr_hunt.views.add_hunt_has') as addit:
                request = MagicMock()
                request.method = "POST"
                #request.POST.get = MagicMock()
                def side_effect(*args):
                    def second_call(*args):
                        return 'testclue'
                    request.POST.get.side_effect = second_call
                    return 'testitem'
                request.POST.get = MagicMock(side_effect=side_effect)
                #request.POST.get('clue', '').return_value = 'testclue'
                #request.POST.get('item', '').return_value = 'testitem'
                request.user = MagicMock()
                attrs = {'is_authenticated.return_value':True}
                request.user.configure_mock(**attrs)
                request.user.username = MagicMock()
                request.user.username.return_value = 'user1'
                views.render_proc_it(request)
                assert request.user.is_authenticated.called
                assert addit.called
                red.assert_called_with('cr_aitem') #check that correct redirect is made
                self.assertEqual(views.i_counter, 1) #counter was incremented
                #test that if item wasn't entered redirect to page
                red.reset_mock()
                def side_effect(*args):
                    def second_call(*args):
                        return ''
                    request.POST.get.side_effect = second_call
                    return 'testclue'
                request.POST.get = MagicMock(side_effect=side_effect)
                addit.reset_mock()
                views.render_proc_it(request)
                assert not(addit.called)
                red.assert_called_with('cr_aitem')
                views.i_counter = 10
                red.reset_mock()
                views.render_proc_it(request)
                red.assert_called_with('cr_end') #check that correct redirect is made
                red.reset_mock()
                attrs = {'is_authenticated.return_value':False}
                request.user.configure_mock(**attrs)
                views.render_proc_it(request)
                assert red.called
                red.assert_called_with('cr_error')

    def test_render_error(self):
        """
            **test_render_error** * Test that rend is called with correct url
        """
        with patch('cr_hunt.views.render_to_response') as rend:
            request = MagicMock()
            views.render_error(request)
            assert rend.called #check that rend is called
            rend.assert_called_with("cr_hunt/cr_hunt_error.html")
##############**** Model Instantiation
    #def test_instantiate(self):


##############**** Model function tests

    def test_add_hunt_its(self): #incomplete
        """
            **test_add_hunt_its** * Test that correct items are added
        """
        with patch('cr_hunt.models.cr_Hunts.objects.create') as cr_obj:
            id_hunt = '123'
            title = 'test title'
            start = 'test start'
            uname = 'user1'
            cr_obj = MagicMock(Title='test title', Start='test start', CreatedBy='user1')
            cr_obj.save = MagicMock(return_value=None)
            #cr_obj.save().return_value = None
            models.add_hunt_its(id_hunt, title, start, uname)
            self.assertEqual(cr_obj.Title, title) # Check that correct title is passed through
            self.assertEqual(cr_obj.Start, start) # Check that correct start point is passed through
            #assert cr_obj.save.called # Check that data save was called

    def test_add_hunt_has(self):
        """
            **test_add_hunt_has** * Test that correct items are added
        """
        with patch('cr_hunt.models.cr_Has.objects.create') as cr_obj:
            with patch('cr_hunt.models.cr_Hunts.objects.get') as geth:
                with patch('cr_hunt.models.Items.objects.get') as geti:
                    id_hunt = '123'
                    nitem = '1122'
                    nnum = 3
                    nclue = 'clue'
                    cr_obj = MagicMock(number=3, clue='clue')
                    cr_obj.save = MagicMock(return_value=None)
                    models.add_hunt_has(id_hunt, nitem, nnum, nclue)
                    self.assertEqual(cr_obj.number, nnum)
                    self.assertEqual(cr_obj.clue, nclue)

    def test_gen_hunt_id(self):
        """
            **test_gen_hunt_id** * Test that a unique id is returned
        """
        with patch('cr_hunt.models.cr_Hunts.objects.filter') as filt:
            #attrs = {'count.return_value':20}
            #filt(CreatedBy = uname).configure_mock(**attrs)
            #filt.return_value = 20
            filt.return_value.count.return_value = 20
            uname = 'bob'
            retname = models.gen_hunt_id(uname)
            self.assertEqual(retname, 'bob20')

    def test_get_cur_count(self):
        """
            **test_get_cur_count** * Test that item number is returned
        """
        with patch('cr_hunt.models.cr_Has.objects.filter') as filt:
            with patch('cr_hunt.models.cr_Hunts.objects.filter') as filth:
                filth.return_value.first.return_value = True
                filt.return_value.count.return_value = 8
                retval = models.get_cur_count('test')
                self.assertEqual(retval, 8)
                filt.reset_mock()
                filth.return_value.first.return_value = False
                retval = models.get_cur_count('test')
                self.assertEqual(retval,0)