# -*- coding: utf-8 -*-
from tests import msg, MockWSGIEnviron as Environ
from uamobile import detect
from uamobile.softbank import SoftbankUserAgent

def test_useragent_softbank():
    def inner(useragent, version, model, packet_compliant,
              serial_number=None, vendor=None, vendor_version=None, java_infos=None):
        ua = detect(Environ(useragent))

        assert isinstance(ua, SoftbankUserAgent)
        assert ua.carrier == 'SoftBank'
        assert ua.short_carrier == 'S'

        assert ua.is_docomo() == False
        assert ua.is_ezweb() == False
        assert ua.is_softbank()
        assert ua.is_vodafone()
        assert ua.is_jphone()
        assert ua.is_willcom() == False
        assert ua.is_nonmobile() == False

        if serial_number:
            assert ua.serialnumber == serial_number, msg(ua, ua.serialnumber, serial_number)
            assert ua.version == version
            assert ua.model == model, msg(ua, ua.model, model)
            assert ua.packet_compliant == packet_compliant

            assert ua.vendor == vendor, msg(ua, ua.vendor, vendor)
            assert ua.vendor_version == vendor_version, msg(ua, ua.vendor_version, vendor_version)

    for args in DATA:
        yield ([inner] + list(args))

#########################
# Test data
#########################

DATA = (
# ua, version, model, packet_compliant, serial_number, vendor, vendor_version, java_infos
    ('J-PHONE/2.0/J-DN02', '2.0', 'J-DN02', False),
    ('J-PHONE/3.0/J-PE03_a', '3.0', 'J-PE03_a', False),
    ('J-PHONE/4.0/J-SH51/SNJSHA3029293 SH/0001aa Profile/MIDP-1.0 Configuration/CLDC-1.0 Ext-Profile/JSCL-1.1.0', '4.0', 'J-SH51', True, 'JSHA3029293', 'SH', '0001aa', { 'Profile':'MIDP-1.0', 'Configuration':'CLDC-1.0', 'Ext-Profile':'JSCL-1.1.0' }),
    ('J-PHONE/4.0/J-SH51/SNXXXXXXXXX SH/0001a Profile/MIDP-1.0 Configuration/CLDC-1.0 Ext-Profile/JSCL-1.1.0', '4.0', 'J-SH51', True, 'XXXXXXXXX', 'SH', '0001a', {'Profile' : 'MIDP-1.0', 'Configuration' : 'CLDC-1.0', 'Ext-Profile' : 'JSCL-1.1.0'}),
    ('J-PHONE/5.0/V801SA SA/0001JP Profile/MIDP-1.0 Configuration/CLDC-1.0 Ext-Profile/JSCL-1.1.0', '5.0', 'V801SA', True),
    ('Vodafone/1.0/V702NK/NKJ001 Series60/2.6 Nokia6630/2.39.148 Profile/MIDP-2.0 Configuration/CLDC-1.1', '1.0', 'V702NK', True, None, 'NK', 'NKJ001', {'Profile' : 'MIDP-1.0', 'Configuration' : 'CLDC-1.0'}),

    # TODO check whether this serial number is valid.
    ('Vodafone/1.0/V702NK/NKJ001/SN123456789012345 Series60/2.6 Nokia6630/2.39.148 Profile/MIDP-2.0 Configuration/CLDC-1.1', '1.0', 'V702NK', True, '123456789012345', 'NK', 'J001', {'Profile' : 'MIDP-1.0', 'Configuration' : 'CLDC-1.0'}),

    # TODO cehck whether this serial number is valid
    ('Vodafone/1.0/V802SE/SEJ001/SN123456789012345 Browser/SEMC-Browser/4.1 Profile/MIDP-2.0 Configuration/CLDC-1.1', '1.0', 'V802SE', True, '123456789012345', 'SE', 'J001', {'Profile' : 'MIDP-2.0', 'Configuration' : 'CLDC-1.1'}),
    ('Vodafone/1.0/V902SH/SHJ001 Browser/UP.Browser/7.0.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 Ext-J-Profile/JSCL-1.2.2 Ext-V-Profile/VSCL-2.0.0', '1.0', 'V902SH', True, None, 'SH', 'J001', {'Profile' : 'MIDP-2.0', 'Configuration' : 'CLDC-1.1'}),
    ('Vodafone/1.0/V802N/NJ001 Browser/UP.Browser/7.0.2.1.258 Profile/MIDP-2.0 Configuration/CLDC-1.1 Ext-J-Profile/JSCL-1.2.2 Ext-V-Profile/VSCL-2.0.0', '1.0', 'V802N', True, None, 'N', 'J001', {'Profile' : 'MIDP-2.0', 'Configuration' : 'CLDC-1.1'}),
    ('MOT-V980/80.2F.2E. MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1', '', 'V980', True, None, 'MOT', '80.2F.2E.', {'Profile' : 'MIDP-2.0', 'Configuration' : 'CLDC-1.1'}),
    ('J-PHONE/3.0/V301SH', '3.0', 'V301SH', False),
    ('J-PHONE/3.0/V301T', '3.0', 'V301T', False),
    ('SoftBank/1.0/705P/PJP10 Browser/Teleca-Browser/3.1 Profile/MIDP-2.0 Configuration/CLDC-1.1', '1.0', '705P', True, None, 'P', 'JP10', {'Profile' : 'MIDP-2.0', 'Configuration' : 'CLDC-1.1'}),
)