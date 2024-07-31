from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('714F587451654D425255346168737842474E562F584D6B7045456276497A6F75785163306B752F494D646B3D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f" {code} کد تایید شما ",
        }
        
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
        
        
class IsAdminUserMixin(UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_authenticated and self.request.user.is_admin
        