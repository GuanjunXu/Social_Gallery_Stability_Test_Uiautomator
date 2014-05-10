#!/usr/bin/env python
from devicewrapper.android import device as d
import time
import unittest
import commands
import string
import util

u = util.Util()

class GalleryTest(unittest.TestCase):

    def setUp(self):
        super(GalleryTest,self).setUp()
        # clear test resource
        #self.util = util.Util
        #u._clearAllResource()
        # push test pics.
        u._confirmResourceExists()
        # launch gallery
        u.launchGallery()


    def tearDown(self):
        super(GalleryTest,self).tearDown()
        #4.Exit activity
        u.pressBack(4)

    # Testcase 1
    def testAlbumsViewSwitchtoPlaces(self):
        """
        Summary:Switch Albums to Places.
        Step:
        1. Launch SocialGallery app
        2. Tap the switch filter
        3. Tap Places filter
        4. Exit SocialGallery app
        """
        # Step 2 + Step 3
        u.selectFilter('Places')
        # confirm switch to Places
        assert d(text = 'Places').wait.exists(timeout = 2000),'switch to Places failed!'

    # Testcase 2
    def testAlbumsViewSwitchtoEvents(self):
        """
        Summary:Switch Albums to Events.
        Step:
        1. Launch SocialGallery app
        2. Tap the switch filter
        3. Tap Events filter
        4. Exit SocialGallery app
        """
        # Step 2 + Step 3
        u.selectFilter('Events')
        # confirm switch to Events
        assert d(text = 'Events').wait.exists(timeout = 2000),'switch to Events failed!'

    # Testcase 3
    def testAlbumsViewSwitchtoDates(self):
        """
        Summary:Switch Albums to Dates.
        Step:
        1. Launch SocialGallery app
        2. Tap the switch filter
        3. Tap Dates filter
        4. Exit SocialGallery app
        """
        # Step 2 + Step 3
        u.selectFilter('Dates')
        # confirm switch to Dates
        assert d(text = 'Dates').wait.exists(timeout = 2000),'switch to Dates failed!'

    # Testcase 4
    def testAlbumsViewSwitchtoPeople(self):
        """
        Summary:Switch Albums to People.
        Step:
        1. Launch SocialGallery app
        2. Tap the switch filter
        3. Tap People filter
        4. Exit SocialGallery app
        """
        # Step 2 + Step 3
        u.selectFilter('People')
        # confirm switch to People
        assert d(text = 'People').wait.exists(timeout = 2000),'switch to People failed!'

    # Testcase 5
    def testSwitchOtherFilterToAlbums(self):
        """
        Summary: Switch to Albums.
        Steps: 
        1. Launch SocialGallery app
        2. Tap the switch filter
        3. Tap another filter except Albums
        4. Tap the switch filter
        5. Tap Albums filter to switch back
        6. Exit SocialGallery app
        """
        # Step 2 + Step 3
        u.selectFilter('People')
        # confirm switch to People
        assert d(text = 'People').wait.exists(timeout = 2000),'switch to People failed!'
        # Step 4 + Step 5
        u.selectFilter('Albums')        
        # confirm switch to Albums
        assert d(text = 'Albums').wait.exists(timeout = 2000),'switch to Albums failed!'

    # Testcase 6
    def testSwitchGalleryToCamera(self):
        """
        Summary: Switch to camera by tap Switch to Camera icon
        Steps: 
        1. Launch SocialGallery app
        2. Tap Switch to Camera Icon
        3. Exit Camera app
        4. Exit SocialGallery app
        """
        # Step 2
        d(description = 'Switch to camera').click.wait(timeout = 1000)
        # If exists the first time of switch camera selection, click social camera and click always.
        if d(text = 'Complete action using').exists:
            d(text = 'com.intel.camera22').click.wait(timeout = 1000)
            d.click(resourceId = 'android:id/button_always')
        # confirm switch to camera.
        assert d(description = 'com.intel.camera22:id/shutter_button').wait.exists
        # Step 3
        u.pressBack(1)

    # Testcase 7
    def testAlbumSocialSync(self):
        """
        Summary: Check Social Sync icon.
        Steps: 
        1. Launch SocialGallery app
        2. Tap Social Sync Icon
        3. Exit SocialGallery app
        """
        # Step 2
        u.setMenuOptions('Social Sync')
        assert d(description = 'Switch to camera').wait.exists

    # Testcase 8
    def testSearchAlbum(self):
        """
        Summary: Check Social Sync icon.
        Steps: 
        1. Launch SocialGallery app
        2. Tap Search Icon
        3. Input the search tag
        4. Exit SocialGallery app
        """
        # Before Searching, a keyword is needed.
        self._longtouchscreencenter()
        u.setMenuOptions('Add a keyword')
        d(text="Enter new keyword").set_text("New Keyword")
        d.click(650,1130)
        # Step 2
        d(description = 'Search').click.wait(timeout = 1000)
        # Step 3
        d(resourceId = 'com.intel.android.gallery3d:id/search_src_text').click.wait()
        d(resourceId = 'com.intel.android.gallery3d:id/search_src_text').set_text('New Keyword')
        # confirm searched item
        assert d(text = 'New Keyword').wait.exists

    # Testcase 9
    def testEnterSocialGallerySettings(self):
        """
        Summary: Enter SocialGallery Settings.
        Steps: 
        1. Launch SocialGallery app
        2. Press menu
        3. Tap Settings
        4. Exit SocialGallery app
        """
        # Step 2 + Step 3
        u.setMenuOptions('Settings')
        # confirm enter to settings
        assert d(text = 'Background Face Recognition').wait.exists

    # Testcase 10
    def testTurnOffOnUpdateNotification(self):
        """
        Summary: Turn off/on Update Notification in SocialGallery settings.
        Steps: 
        1. Launch SocialGallery app
        2. Press menu
        3. Tap Settings
        4. Tap Update Notifications to turn it off
        5. Tap Update Notifications to turn it on
        6. Exit SocialGallery app
        """
        # Step 2 + Step 3
        u.setMenuOptions('Settings')
        # step 4
        d(text = 'Update Notification').click()
        result = commands.getoutput('adb shell cat data/data/com.intel.android.gallery3d/shared_prefs/SocialGallery2.0_Pref.xml | grep background_fr_notification')
        if result.find('false') == -1:
            self.fail('turn Update Notification failed')
        # step 5
        d(text = 'Update Notification').click()
        time.sleep(2)
        result = commands.getoutput('adb shell cat data/data/com.intel.android.gallery3d/shared_prefs/SocialGallery2.0_Pref.xml| grep background_fr_notification')
        if result.find('true') == -1:
            self.fail('turn Update Notification failed')

    # Testcase 11
    def testSortByName(self):
        """
        Summary: Sort album by name A-Z&Z-A.
        Steps: 
        1. Launch SocialGallery app
        2. Press menu
        3. Tap Sort by name A-Z
        4. Press menu
        5. Tap Sort by name Z-A
        6. Exit SocialGallery app
        """
        # Step 2 + Step 3
        u.setMenuOptions('Sort by name, A-Z')
        assert d(description = 'Switch to camera').wait.exists
        # step 4 + step 5
        u.setMenuOptions('Sort by name, Z-A')
        assert d(description = 'Switch to camera').wait.exists

    # Testcase 12
    def testSortByRecentAscending(self):
        """
        Summary: Sort album by recent ascending&descending
        Steps: 
        1. Launch SocialGallery app
        2. Press menu
        3. Tap Sort by recent ascending
        4. Press menu
        5. Tap Sort by recent descending
        6. Exit SocialGallery app
        """
        # Step 2 + Step 3
        u.setMenuOptions('Sort by recent, ascending')
        assert d(text = 'Sort by recent, descending').wait.exists
        # step 4 + step 5
        u.setMenuOptions('Sort by recent, descending')
        assert d(description = 'Switch to camera').wait.exists

    # Testcase 13
    def testCheckAlbumDetail(self):
        """
        Summary: Check details
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap Extra menu Icon
        4. Tap Details option
        5. Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4
        u.setMenuOptions('Details')
        # confirm pop up details dialog
        assert d(text = '1 of 2 items:').wait.exists

    # Testcase 14
    def testAddKeywordsToAlbum(self):
        """
        Summary: Add keywords
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album to select it
        3. Tap Extra Menu
        4. Tap Add keywords option
        5. Input keywords
        6. Tap Save button
        7. Exit SocialGallery app
        """
        # Step 2 
        self._longtouchscreencenter()
        # Step 3 + Step 4
        u.setMenuOptions('Add a keyword')
        # Step 5
        d(text="Enter new keyword").set_text("New Keyword")
        # Step 6
        d.click(650,1130)
        # confirm add keywords
        self._longtouchscreencenter()
        u.setMenuOptions('Add a keyword')
        assert d(text = 'New Keyword').wait.exists

    # Testcase 15
    def testShareAlbumViaGooglePlus(self):
        """
        Summary: Share album via Google+
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap share icon
        4. Tap See all option
        5. Tap Google+ option
        6. Back to SocialGallery app
        7. Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4 + Step 5
        u.shareItem('Google+')
        # confirm enter Google+
        assert d(packageName = 'com.google.android.apps.plus').wait.exists(timeout = 2000)
        u.pressBack(1)
        d(text = 'Yes').click()

    # Testcase 16
    def testShareAlbumViaMessaging(self):
        """
        Summary: Share album via Messaging
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap share icon
        4. Tap See all option
        5. Tap Messaging option
        6. Back to SocialGallery app
        7. Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4 + Step 5
        u.shareItem('Messaging')
        # confirm enter Messaging
        assert d(text = 'New message').wait.exists(timeout = 2000)
        # Step 6
        u.pressBack(2)
        d(text = 'OK').click()

    # Testcase 17
    def testShareAlbumViaPicasa(self):
        """
        Summary: Share album via Picasa
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap share icon
        4. Tap See all option
        5. Tap Picasa option
        6. Back to SocialGallery app
        7.Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4 + Step 5
        u.shareItem('Picasa')
        # confirm enter Picasa
        assert d(text = 'Upload 20 photos/videos').wait.exists(timeout = 2000)

    # Testcase 18
    def testShareAlbumViaGmail(self):
        """
        Summary: Share album via Gmail
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap share icon
        4. Tap See all option
        5. Tap Gmail option
        6. Back to SocialGallery app
        7.Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4 + Step 5
        u.shareItem('Gmail')
        # confirm enter Gamil
        assert d(text = 'Gmail').wait.exists(timeout = 2000)

    # Testcase 19
    def testShareAlbumViaDrive(self):
        """
        Summary: Share album via Drive
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap share icon
        4. Tap See all option
        5. Tap Drive option
        6. Back to SocialGallery app
        7.Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4 + Step 5
        u.shareItem('Drive')
        # confirm enter Driver
        assert d(text = 'Upload to Drive').wait.exists(timeout = 2000)

    # Testcase 20
    def testShareAlbumViaYouTube(self):
        """
        Summary: Share album via YouTube
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap share icon
        4. Tap See all option
        5. Tap YouTube option
        6. Back to SocialGallery app
        7.Exit SocialGallery app
        """
        u._prepareVideo()
        time.sleep(2)
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4 + Step 5
        u.shareItem('YouTube')
        # confirm enter YouTube
        assert d(text = 'Choose an account').wait.exists(timeout = 2000)

    # Testcase 21
    def testShareAlbumViaFacebook(self):
        """
        Summary: Share album via Facebook
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap share icon
        4. Tap See all option
        5. Tap Facebook option
        6. Back to SocialGallery app
        7.Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4 + Step 5
        u.shareItem('Facebook')
        # confirm enter Facebook
        assert d(text = 'Loading...').wait.exists(timeout = 2000)

    # Testcase 22
    def testShareAlbumViaBluetooth(self):
        """
        Summary: Share album via Bluetooth
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap share icon
        4. Tap See all option
        5. Tap Bluetooth option
        6. Back to SocialGallery app
        7.Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4 + Step 5
        u.shareItem('Bluetooth')
        # confirm enter Bluetooth
        assert d(text = 'Bluetooth device chooser').wait.exists(timeout = 2000)

    # Testcase 23
    def testDeleteAlbum(self):
        """
        Summary: Delete an album
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap Delete icon
        4. Select Delete option to confirm delete
        5. Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4
        u.deleteItem('Delete')
        time.sleep(2)
        # confirm Delete complete
        result = commands.getoutput('adb shell ls -l /sdcard/testalbum/testpictures1 | grep jpg | wc -l')
        if string.atoi(result) != 0:
            self.fail('delete failed in 2s!')

    # Testcase 24
    def testCancelDeleteAlbum(self):
        """
        Summary: Cancel Delete an album
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album thumbnail to select it
        3. Tap Delete icon
        4. Select Cancle option to cancel delete
        5. Exit SocialGallery app
        """
        # Step 2 
        d.swipe(355,575,356,576)
        # Step 3 + Step 4
        u.deleteItem('Cancel')
        # confirm Delete complete
        result = commands.getoutput('adb shell ls -l /sdcard/testalbum/testpictures1 | grep jpg | wc -l')
        if string.atoi(result) == 0:
            self.fail('Cancel delete failed!')

    # Testcase 25
    def testCancelDeleteAllAlbum(self):
        """
        Summary: Cancel Delete all album
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album to select it
        3. Tap Select Album Dropdown
        4. Select Select all option to select all the albums
        5. Tap Delete icon
        6. Tap Cancel Delete option
        7. Exit SocialGallery app
        """
        # Step 2
        d.swipe(355,575,356,576)
        # Step 3
        d(text = '1 selected').click()
        # Step 4
        d(text = 'Select all').click()
        # Step 5 + Step 6
        u.deleteItem('Cancel')
        # confirm Cancel Delete complete
        result = commands.getoutput('adb shell ls -l /sdcard/testalbum/testpictures1 | grep jpg | wc -l')
        if string.atoi(result) == 0:
            self.fail('Cancel delete failed!')

    # Testcase 26
    def testSelectDeselectAllAlbums(self):
        """
        Summary: select albums via long tap on the album, then select all, deselect all albums
        Steps: 
        1. Launch SocialGallery app
        2. Long tap on an album to select it
        3. Tap Select Album Dropdown
        4. Tap Select all option
        5. Tap Select Album Dropdown
        6. Tap Deselect all option
        7. Exit SocialGallery app
        """
        # Step 2 + Step 3
        d.swipe(355,575,356,576)
        d(text = '1 selected').click()        
        # Step 4
        d(text = 'Select all').click()
        assert d(description = 'Switch to camera').wait.exists
        # Step 5
        d(text = '2 selected').click()
        # Step 6
        d(text = 'Deselect all').click()
        assert d(description = 'Switch to camera').wait.exists

    def _longtouchscreencenter(self):
        d.swipe(350,700,351,701)