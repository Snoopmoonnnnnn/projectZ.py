from time import time
from uuid import uuid4

class Headers:
	def __init__(self, deviceId: str, sid: str = None, time_zone: int = 180, country_code: str = "en", language: str = "en-US"):
		self.sid = sid
		self.deviceId = deviceId
		self.time_zone = time_zone
		self.country_code = country_code
		self.language = language

	def Headers(self):

		headers = {
			"rawDeviceId": "0436103c274039ff6e0755d8003a7852a1945755d4ca8c5d2f4b88bebb42a5fc3631c8c5b85c96740b",#self.deviceId,
			"nonce": str(uuid4()),
			"Accept-Language": self.language,
			"countryCode": self.country_code.upper(),
			"carrierCountryCodes": self.country_code,
			"timeZone": str(self.time_zone),
			"reqTime": str(int(time() * 1000)),
			"sId": self.sid if self.sid else ''
		}

		return headers

	def get_persistent_headers(self) -> dict: return {
            "appType": "MainApp", "appVersion": "2.27.1",
            "osType": "2", "deviceType": "1", "flavor": "google",
            "User-Agent": "com.projz.z.android/2.27.1-25104 (Linux; U; Android 7.1.2; ASUS_Z01QD; Build/Asus-user 7.1.2 2017)"
        }
