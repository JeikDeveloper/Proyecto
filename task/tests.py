from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework import status

class MethodTest(TestCase):

    def test_get_method(self):
        """ Comprobar la correcta visualización de get """
        response = self.client.get('/tasks/')

        self.assertEqual(response.status_code, 200)

    def test_create_user_with_email_successful(self):
        """ Probar, crear un nueva tarea correctamente """
        
        username = 'test'
        name= 'Tasks'
        user = get_user_model().objects.create_user(
            name=name,
            username=username
        )

        self.assertEqual(user.name, name)
        self.assertTrue(user.username, username)

    def test_new_user_email_normalized(self):
        """ Testea email para nuevo usuario normalizado """

        email = 'test@DaTadosis.COM'
        user = get_user_model().objects.create_user(email, 'Testpass123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Nuevo usuario email invalido """

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None, 'Testpass123')

    def test_create_new_superuser(self):
        """ Probar super usuario creado """

        email = 'test@datadosis.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_tasks(self):
        """ Comprobar el subir un archivo """
        with open("tasks/tests/resources/archivo_prueba.csv", mode="rb") as file:
            file = SimpleUploadedFile(
                file.name, file.read(), content_type='file/csv'
            )
            sopport_file = file
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)