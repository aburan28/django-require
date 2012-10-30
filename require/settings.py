from django.conf import settings


REQUIRE_BASE_URL = getattr(settings, "REQUIRE_BASE_URL", "js")

REQUIRE_BUILD_PROFILE = getattr(settings, "REQUIRE_BUILD_PROFILE", "app.build.js")

REQUIRE_JS = getattr(settings, "REQUIRE_JS", "require.js")