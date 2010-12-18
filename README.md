# fmi

A small Python library to fetch location information from the "Find My iPhone"
service on MobileMe.

## Example

    from fmi import FMI
        
    fmi = FMI('myusername@me.com', 'mypassword')
    fmi.login()

    devices = fmi.devices()

    for device in devices['content']:
        print device['name'], '-',
        if not device['location']:
            print 'No location found'
            continue
        print device['location']['longitude'],
        print device['location']['latitude']

Will display all devices registered with MobileMe's Find My iPhone. An example
output is:

    Batman's iPhone - 151.204420924 -33.85947118
    Batman’s iPad - No location found

## Notes

This is a quick hack right now, but might slowly improve over time.

## Bugs

The domain changes (when calling devices) and there is no detection for it yet.
This means it might be completely broken for you. A fix is coming soon.
