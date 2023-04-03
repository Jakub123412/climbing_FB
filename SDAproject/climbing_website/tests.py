from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

from .models import Localization, Country, Rock, Insolation, Formation


class UserAuthorizationTest(TestCase):
    def setUp(self):
        test_user = User(username="user1234")
        test_user.set_password("dhfef121feefx4d1")
        test_user.save()
        self.client.login(username="user1234", password="dhfef121feefx4d1")

    def test_user_login(self):
        response = self.client.get(reverse("search"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "climbing_website/search.html")
        self.assertEqual(str(response.context["user"]), "user1234")

    def test_user_logout(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertNotEquals("user", response.context)
        self.assertRedirects(response, reverse("login"))


class SearchTest(TestCase):
    def setUp(self) -> None:
        test_user = User(username="user1234")
        test_user.set_password("dhfef121feefx4d1")
        test_user.save()

        insolation = Insolation(name="north")
        insolation.save()

        formation = Formation(name="vertical")
        formation.save()

        country = Country(country_number="PL", country_name="Polska")
        country.save()

        localization = Localization(country=country, district= "Małoposka", region= "Brama Krakowska", subregion= "Skay Niepeickie", rock_groups="Groszówka")
        localization.save()

        rock = Rock(rock_name= "Złotówka", height = 7, insolation= insolation, formation= formation, localization = localization )
        rock.save()

        rock = Rock(rock_name="Żagiel", height=10, insolation=insolation, formation=formation,
                    localization=localization)
        rock.save()

        rock = Rock(rock_name="Zig-Zak", height=15, insolation=insolation, formation=formation,
                    localization=localization)
        rock.save()

        self.client.login(username="user1234", password="dhfef121feefx4d1")

    def test_all_rocks_shown(self):
        response = self.client.get(reverse("search"))
        self.assertEqual(str(response.context["user"]), "user1234")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("rocks" in response.context)
        self.assertEqual(len(response.context["rocks"]), 3)
