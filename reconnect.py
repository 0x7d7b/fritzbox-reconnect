import requests


def reconnect():

    soap_body = (
        '\r\n'
        '<?xml version="1.0" encoding="utf-8"?>'
        '<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">'
        '  <s:Body>'
        '    <u:ForceTermination xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:2"/>'
        '  </s:Body>'
        '</s:Envelope>'
    )
    soap_body_raw = bytes(soap_body, encoding='utf-8')

    soap_action = "urn:schemas-upnp-org:service:WANIPConnection:2#ForceTermination"

    headers = {
        'SOAPAction': f'{soap_action}',
        'Host': 'fritz.box:49000',
        'Content-Type': 'text/xml; charset=utf-8',
        'Content-Length': str(len(soap_body_raw))
    }

    ctrl_url = "http://fritz.box:49000/igd2upnp/control/WANIPConn1"

    return requests.request(
        method='post',
        url=ctrl_url,
        data=soap_body_raw,
        headers=headers
    )


if __name__ == '__main__':
    response = reconnect()
    print(response.text)
    if 200 != response.status_code:
        exit(1)
