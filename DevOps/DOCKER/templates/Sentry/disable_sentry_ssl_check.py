# pip install sentry_sdk

import sentry_sdk

...

def disable_sentry_ssl_check():
    # disable sni warnings
    import urllib3
    urllib3.disable_warnings()

    def _get_pool_options(self, ca_certs):
        return {
            "num_pools": 2,
            "cert_reqs": "CERT_NONE",
        }

    # disable ssl check
    from sentry_sdk.transport import HttpTransport
    HttpTransport._get_pool_options = _get_pool_options 

...

disable_sentry_ssl_check()
sentry_sdk.init(...)

...