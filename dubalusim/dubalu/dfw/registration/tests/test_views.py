# -*- coding: utf-8 -*-
"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:copyright: Copyright (c) 2007-2012, James Bennett.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

import datetime

from django.test import TestCase
from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from .. import forms
from ..models import RegistrationProfile


class RegistrationViewTests(TestCase):
    """
    Test the registration views.

    """
    urls = 'dfw.registration.tests.urls'

    def setUp(self):
        """
        These tests use the default backend, since we know it's
        available; that needs to have ``ACCOUNT_ACTIVATION_DAYS`` set.

        """
        self.old_activation = getattr(
            settings, 'ACCOUNT_ACTIVATION_DAYS', None)
        if self.old_activation is None:
            settings.ACCOUNT_ACTIVATION_DAYS = 7  # pragma: no cover

    def tearDown(self):
        """
        Yank ``ACCOUNT_ACTIVATION_DAYS`` back out if it wasn't
        originally set.

        """
        if self.old_activation is None:
            settings.ACCOUNT_ACTIVATION_DAYS = self.old_activation  # pragma: no cover

    def test_registration_view_initial(self):
        """
        A ``GET`` to the ``register`` view uses the appropriate
        template and populates the registration form into the context.

        """
        response = self.client.get(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'registration/registration_form.html')
        self.failUnless(isinstance(response.context['form'],
                                   forms.RegistrationForm))

    def test_registration_view_success(self):
        """
        A ``POST`` to the ``register`` view with valid data properly
        creates a new user and issues a redirect.

        """
        response = self.client.post(reverse('registration_register'),
                                    data={'email': 'alice@example.com',
                                          'password1': 'swordfish',
                                          'password2': 'swordfish'})
        self.assertRedirects(response,
                             'http://testserver%s' % reverse('registration_complete'))
        self.assertEqual(RegistrationProfile.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)

    def test_registration_view_failure(self):
        """
        A ``POST`` to the ``register`` view with invalid data does not
        create a user, and displays appropriate error messages.

        """
        response = self.client.post(reverse('registration_register'),
                                    data={'email': 'bobe@example.com',
                                          'password1': 'foo',
                                          'password2': 'bar'})
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response, 'form', field=None,
                             errors=u"The two password fields didn't match.")
        self.assertEqual(len(mail.outbox), 0)

    def test_registration_view_closed(self):
        """
        Any attempt to access the ``register`` view when registration
        is closed fails and redirects.

        """
        old_allowed = getattr(settings, 'REGISTRATION_OPEN', True)
        settings.REGISTRATION_OPEN = False

        closed_redirect = 'http://testserver%s' % reverse(
            'registration_disallowed')

        response = self.client.get(reverse('registration_register'))
        self.assertRedirects(response, closed_redirect)

        # Even if valid data is posted, it still shouldn't work.
        response = self.client.post(reverse('registration_register'),
                                    data={'email': 'alice@example.com',
                                          'password1': 'swordfish',
                                          'password2': 'swordfish'})
        self.assertRedirects(response, closed_redirect)
        self.assertEqual(RegistrationProfile.objects.count(), 0)

        settings.REGISTRATION_OPEN = old_allowed

    def test_registration_template_name(self):
        """
        Passing ``template_name`` to the ``register`` view will result
        in that template being used.

        """
        response = self.client.get(reverse(
            'registration_test_register_template_name'))
        self.assertTemplateUsed(response,
                                'registration/test_template_name.html')

    def test_registration_extra_context(self):
        """
        Passing ``extra_context`` to the ``register`` view will
        correctly populate the context.

        """
        response = self.client.get(reverse(
            'registration_test_register_extra_context'))
        self.assertEqual(response.context['foo'], 'bar')
        # Callables in extra_context are called to obtain the value.
        self.assertEqual(response.context['callable'], 'called')

    def test_registration_disallowed_url(self):
        """
        Passing ``disallowed_url`` to the ``register`` view will
        result in a redirect to that URL when registration is closed.

        """
        old_allowed = getattr(settings, 'REGISTRATION_OPEN', True)
        settings.REGISTRATION_OPEN = False

        closed_redirect = 'http://testserver%s' % reverse(
            'registration_test_custom_disallowed')

        response = self.client.get(reverse(
            'registration_test_register_disallowed_url'))
        self.assertRedirects(response, closed_redirect)

        settings.REGISTRATION_OPEN = old_allowed

    def test_registration_success_url(self):
        """
        Passing ``success_url`` to the ``register`` view will result
        in a redirect to that URL when registration is successful.

        """
        success_redirect = 'http://testserver%s' % reverse(
            'registration_test_custom_success_url')
        response = self.client.post(
            reverse('registration_test_register_success_url'),
            data={'email': 'alice@example.com',
                  'password1': 'swordfish',
                  'password2': 'swordfish'})
        self.assertRedirects(response, success_redirect)

    def test_valid_activation(self):
        """
        Test that the ``activate`` view properly handles a valid
        activation (in this case, based on the default backend's
        activation window).

        """
        User = get_user_model()
        success_redirect = 'http://testserver%s' % reverse(
            'registration_activation_complete')

        # First, register an account.
        self.client.post(reverse('registration_register'),
                         data={'email': 'alice@example.com',
                               'password1': 'swordfish',
                               'password2': 'swordfish'})
        profile = RegistrationProfile.objects.get(user__email='alice@example.com')
        response = self.client.get(reverse('registration_activate',
                                           kwargs={'activation_key': profile.activation_key}))
        self.assertRedirects(response, success_redirect)
        self.failUnless(User.objects.get(email='alice@example.com').is_active)

    def test_invalid_activation(self):
        """
        Test that the ``activate`` view properly handles an invalid
        activation (in this case, based on the default backend's
        activation window).

        """
        User = get_user_model()
        # Register an account and reset its date_joined to be outside
        # the activation window.
        self.client.post(reverse('registration_register'),
                         data={'email': 'bob@example.com',
                               'password1': 'secret',
                               'password2': 'secret'})
        expired_user = User.objects.get(email='bob@example.com')
        expired_user.date_joined = expired_user.date_joined - \
            datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        expired_user.save()

        expired_profile = RegistrationProfile.objects.get(user=expired_user)
        response = self.client.get(reverse('registration_activate',
                                           kwargs={'activation_key': expired_profile.activation_key}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['activation_key'],
                         expired_profile.activation_key)
        self.failIf(User.objects.get(email='bob@example.com').is_active)

    def test_activation_success_url(self):
        """
        Passing ``success_url`` to the ``activate`` view and
        successfully activating will result in that URL being used for
        the redirect.

        """
        success_redirect = 'http://testserver%s' % reverse(
            'registration_test_custom_success_url')
        response = self.client.post(reverse('registration_register'),
                         data={'email': 'alice@example.com',
                               'password1': 'swordfish',
                               'password2': 'swordfish'})
        self.assertEqual(response.status_code, 302)
        profile = RegistrationProfile.objects.get(user__email='alice@example.com')
        response = self.client.get(
            reverse('registration_test_activate_success_url',
                    kwargs={'activation_key': profile.activation_key}))
        self.assertRedirects(response, success_redirect)

    def test_activation_template_name(self):
        """
        Passing ``template_name`` to the ``activate`` view will result
        in that template being used.

        """
        response = self.client.get(
            reverse('registration_test_activate_template_name',
                    kwargs={'activation_key': 'foo'}))
        self.assertTemplateUsed(
            response, 'registration/test_template_name.html')

    def test_activation_extra_context(self):
        """
        Passing ``extra_context`` to the ``activate`` view will
        correctly populate the context.

        """
        response = self.client.get(
            reverse('registration_test_activate_extra_context',
                    kwargs={'activation_key': 'foo'}))
        self.assertEqual(response.context['foo'], 'bar')
        # Callables in extra_context are called to obtain the value.
        self.assertEqual(response.context['callable'], 'called')
