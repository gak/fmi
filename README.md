# fmi

A small utility to fetch location information from the "Find My iPhone" service on mobile.me.

## Example

    from fmi import FMI
    self.fmi = FMI('myusername@me.com', 'mypassword')
    print self.fmi.devices()

Will return a dictionary with many details include GPS co-ordinates.

## Notes

This is a quick hack right now, but might slowly improve over time.

