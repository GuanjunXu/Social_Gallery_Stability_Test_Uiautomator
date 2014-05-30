#!/usr/bin/env python
from uiautomatorplug.android import device as d
import time
import unittest
import commands
import string
import util
import random

u = util.Util()
SCREEN_Center_Pox = (350,700)
SLIDESHOW_OPTION = ['Cine Effect','Dissolve','Flash']

class GalleryTest(unittest.TestCase):

    def setUp(self):
        super(GalleryTest,self).setUp()
        #Add on May 26th due to device always reboot by itself
        if d(text = 'Charged').wait.exists(timeout = 2000):
            commands.getoutput('adb root')
            time.sleep(5)
            commands.getoutput('adb remount')
            d.swipe(360,980,719,980)
        # clear test resource
        #self.util = util.Util
        u._clearAllResource()
        # push test pics.
        u._confirmResourceExists()
        # launch gallery
        u.launchGallery()
        # enter grid view
        u.enterXView('gridview')
        # confirm enter gridview
        #assert d(text = 'testpictures2').wait.exists(timeout = 2000)

    def tearDown(self):
        super(GalleryTest,self).tearDown()
        #4.Exit activity
        u.pressBack(4)
        #Force close tap on OK
        if d(text = 'OK').wait.exists(timeout = 2000):
            d(text = 'OK').click.wait()
            u.pressBack(4)

    # Testcase 1
    def testGridViewSwitchtoAlbumsView(self):
        """
        Summary:Switch from Grid View to Album View.
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Tap upnavigation icon
        """
        # Step 3
        d(resourceId = 'android:id/up').click.wait()
        #d(text = 'testpictures2').click()
        # confirm back to album view
        assert d(text = 'Albums').wait.exists(timeout = 2000),'switch to Album view failed!'

    # Testcase 2
    def testSearchKeywordsInGridView(self):
        """
        Summary:Search keywords picture.
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Tap search icon
        4.Input your owner custom keywords.
        5.Touch the searched pics 
        """
        # before searching, a keyword is needed. this step is used to add keyword.
        self._longtouchscreencenter()
        u.setMenuOptions('Add a keyword')
        d(text="Enter new keyword").set_text("New Keyword")
        d.click(650,1130) # click 'done' icon on the keyboard.
        # Step 3
        d(description = 'Search').click()
        # Step 4
        d(resourceId = 'com.intel.android.gallery3d:id/search_src_text').set_text('New Keyword')
        # confirm searched item
        #assert d(text = 'New Keyword (1)').wait.exists(timeout = 2000)

    # Testcase 3
    def testPlaySlideshowWithCineEffect(self):
        """
        Summary:Play slideshow with Cine Effect mode.
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Tap play slideshow icon
        4.Tap Cine Effect option 
        """
        # Step 3
        u.setMenuOptions('Slideshow')
        # Step 4
        d(text = 'Cine Effect').click()
        time.sleep(3)
        # Since automation can't check this point, if it back to gridview treat it as pass.
        u.pressBack(1)
        assert d(description = 'Switch to camera').wait.exists(timeout = 2000)

    # Testcase 4
    def testPlaySlideshowWithDissolve(self):
        """
        Summary:Play slideshow with Dissolve mode.
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Tap play slideshow icon
        4.Tap Dissolve option 
        """
        # Step 3
        u.setMenuOptions('Slideshow')
        # Step 4
        d(text = 'Dissolve').click()
        time.sleep(3)
        # Since automation can't check this point, if it back to gridview treat it as pass.
        u.pressBack(1)
        assert d(description = 'Switch to camera').wait.exists(timeout = 2000)

    # Testcase 5
    def testPlaySlideshowWithFlash(self):
        """
        Summary:Play slideshow with Flash mode.
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Tap play slideshow icon
        4.Tap Flash option 
        """
        # Step 3
        u.setMenuOptions('Slideshow')
        # Step 4
        d(text = 'Flash').click()
        time.sleep(3)
        # Since automation can't check this point, if it back to gridview treat it as pass.
        u.pressBack(1)
        assert d(description = 'Switch to camera').wait.exists(timeout = 2000)

    # Testcase 6
    def testShareIconAvilibaleInGridView(self):
        """
        Summary:Share Option Icon matches with the Share Option Label
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4
        u.shareItem()
        # confirm share icon worked.
        assert d(text = 'See all').wait.exists(timeout = 2000)

    # Testcase 7
    def testSharePictureInGridViewWithBluetooth(self):
        """
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        5.Tap Bluetooth option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5 
        u.shareItem('Bluetooth')
        if d(text = 'Turn on').wait.exists(timeout = 2000):
            d(text = 'Turn on').click.wait()
        # confirm enter Bluetooth
        assert d(text = 'Bluetooth device chooser').wait.exists(timeout = 2000)

    # Testcase 8
    def testSharePictureInGridViewWithPicasa(self):
        """
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        5.Tap Picasa option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5 
        u.shareItem('Picasa')
        # confirm enter Picasa
        assert d(text = 'Upload photo/video').wait.exists(timeout = 2000)

    # Testcase 9
    def testSharePictureInGridViewWithMessaging(self):
        """
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        5.Tap Messaging option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5 
        u.shareItem('Messaging')
        # confirm enter Messaging
        assert d(text = 'New message').wait.exists(timeout = 2000)
        u.pressBack(2)
        d(text = 'OK').click()

    # Testcase 9
    def testSharePictureInGridViewWithOrkut(self):
        """
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        5.Tap Orkut option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5 
        u.shareItem('Orkut')
        # confirm enter Orkut
        assert d(packageName = 'com.google.android.apps.orkut').wait.exists(timeout = 2000)

    # Testcase 10
    def testSharePictureInGridViewWithGooglePlus(self):
        """
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        5.Tap GooglePlus option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5 
        u.shareItem('Google+')
        if d(text = 'Choose account').exists:
            d(text = 'xiaobowen1002@gmail.com').click()
        # confirm enter Google+
        assert d(packageName = 'com.google.android.apps.plus').wait.exists(timeout = 2000)
        u.pressBack(1)
        d(text = 'Yes').click()

    # Testcase 11
    def testSharePictureInGridViewWithGmail(self):
        """
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        5.Tap Gmail option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5 
        u.shareItem('Gmail')
        # confirm enter Gmail
        assert d(text = 'Compose').wait.exists(timeout = 2000)

    # Testcase 12
    def testSharePictureInGridViewWithFacebook(self):
        """
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        5.Tap Facebook option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5 
        u.shareItem('Facebook')
        # confirm enter Gmail
        assert d(text = 'Loading...').wait.exists(timeout = 2000)

    # Testcase 13
    def testSharePictureInGridViewWithYouTube(self):
        """
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        5.Tap YouTube option
        """
        u._prepareVideo()
        time.sleep(2)
        # Step 3
        d.swipe(355,575,356,576)
        # Step 4 + Step 5
        u.shareItem('YouTube')
        # confirm enter YouTube
        assert d(text = 'Choose an account').wait.exists(timeout = 2000)

    # Testcase 14
    def testSharePictureInGridViewWithDrive(self):
        """
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap share icon
        5.Tap Drive option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        u.shareItem('Drive')
        # confirm enter Drive
        assert d(text = 'Upload to Drive').wait.exists(timeout = 2000)

    # Testcase 15
    def testDeleteOnePictureInGridView(self):
        """
        Summary: delete the selected pics or vides
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select
        4.Tap Trash icon
        5.Tap Delete option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        u.deleteItem('Delete')
        time.sleep(3)
        # confirm picture deleted.
        result = commands.getoutput('adb shell ls -l /sdcard/testalbum/testpictures2 | grep jpg | wc -l')
        if string.atoi(result) != 19:
            self.fail('delete failed!')

    # Testcase 16
    def testDeleteMultiplePictureInGridView(self):
        """
        Summary: delete the selected pics or vides
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or a video to select 
        4.Tap another two file to select
        5.Tap Trash icon
        6.Tap Delete option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4
        d.click(100,300)
        d.click(100,500)
        # Step 5 + Step 6
        u.deleteItem('Delete')
        # confirm picture deleted.
        time.sleep(2)
        result = commands.getoutput('adb shell ls -l /sdcard/testalbum/testpictures2 | grep jpg | wc -l')
        if string.atoi(result) != 17:
            self.fail('delete failed!')

    # Testcase 17
    def testEditInGridView(self):
        """
        Summary: edit in grid view
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic to select
        4.Tap Extra Menu
        5.Tap Edit option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        u.setMenuOptions('Edit')
        # select social gallery to edit.
        #d(text = 'com.intel.android.gallery3d').click()
        # confirm enter gallery editer.
        assert d(resourceId = 'com.intel.android.gallery3d:id/fxButton').wait.exists(timeout = 2000)

    # Testcase 18
    def testRotateLeftInGridView(self):
        """
        Summary: Rotate left in grid view
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic to select
        4.Tap Extra Menu
        5.Tap Rotate left option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 5
        u.setMenuOptions('Rotate left')
        # since rotation point could not be checked, if it back to grid view, we treat it as pass.
        assert d(description = 'Switch to camera').wait.exists(timeout = 2000)

    # Testcase 19
    def testRotateRightInGridView(self):
        """
        Summary: Rotate left in grid view
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic to select
        4.Tap Extra Menu
        5.Tap Rotate right option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 5
        u.setMenuOptions('Rotate right')
        # since rotation point could not be checked, if it back to grid view, we treat it as pass.
        assert d(description = 'Switch to camera').wait.exists(timeout = 2000)

    # Testcase 20
    def testCropInGridView(self):
        """
        Summary: crop in grid view
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic to select
        4.Tap Extra Menu
        5.Tap Crop option
        6.Tap CROP icon
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 5
        u.setMenuOptions('Crop')
        if  d(text = 'Complete action using').exists:
            d(text = 'com.intel.android.gallery3d').click()
            d(text = 'Always').click()
        d(text = 'Crop').click()
        result = commands.getoutput('adb shell ls -l /sdcard/testalbum/testpictures2 | grep jpg | wc -l')
        if string.atoi(result) != 21:
            self.fail('crop failed!')

    # Testcase 21
    def testSetPictureAsContactPhotoInGridView(self):
        """
        Summary: Set picture as(Contact photo/Wallpaper)
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic to select
        4.Tap Extra Menu
        5.Tap Set picture as option
        6.Tap Contact photo
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        u.setMenuOptions('Set picture as')
        # Step 6
        self._setpictureas('Contact photo')
        # confirm enter contact
        assert d(packageName = 'com.android.contacts').wait.exists(timeout = 2000)

    # Testcase 22
    def testSetPictureAsWallpaperInGridView(self):
        """
        Summary: Set picture as(Contact photo/Wallpaper)
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic to select
        4.Tap Extra Menu
        5.Tap Set picture as option
        6.Tap Wallpaper
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        u.setMenuOptions('Set picture as')
        # Step 6
        self._setpictureas('Wallpaper')
        d(text = 'Crop').click.wait()
        # confirm back to gallery
        assert d(description = 'Switch to camera').wait.exists(timeout = 2000)

    # Testcase 23
    def testCheckDetailsInGridView(self):
        """
        Summary: Check detail
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic to select
        4.Tap Extra Menu
        5.Tap Details option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        u.setMenuOptions('Details')
        # confirm enter details
        assert d(text = 'Keywords').wait.exists(timeout = 2000)

    # Testcase 24
    def testAddKeywordsInGridView(self):
        """
        Summary: Add keywords in grid view
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic to select
        4.Tap Extra Menu
        5.Tap Add keywords option
        6.Type own custom tags
        7.Tap Save button
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        u.setMenuOptions('Add a keyword')
        # Step 6 + Step 7
        d(text="Enter new keyword").set_text("New Keyword")
        d.click(650,1130) # click 'done' icon on the keyboard.

    # Testcase 25
    def testAnimateInGridView(self):
        """
        Summary: animate picture in gallery
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Select two or more pics
        4.Tap Extra Menu
        5.Tap animate option
        6.Random select the options
        7.Tap create button
        """
        # Step 3 + Step 4
        self._longtouchscreencenter()
        d.click(100,300)
        d.click(100,500)
        # Step 4 + Step 5
        u.setMenuOptions('Animate')
        # Step 6 + Step 7
        d(text = 'Animated GIF').click()
        d(text = 'Create').click()
        time.sleep(2)
        d(text = 'Save').click.wait()
        time.sleep(2)
        # confirm create complete
        result = commands.getoutput('adb shell ls -l /sdcard/Sharing | grep gif | wc -l')
        if string.atoi(result) != 1:
            self.fail('animated failed')

    # Testcase 26
    def testRotateAllInGridView(self):
        """
        Summary: rotate all in grid view
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or video to select
        4.Tap select file dropdown
        5.Tap select all option
        6.Tap extra menu
        7.Tap Rotate left/Rotate right
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        d(text = '1 selected').click()
        d(text = 'Select all').click()
        # Step 6 + Step 7
        u.setMenuOptions('Rotate left')
        time.sleep(2)
        self._longtouchscreencenter()
        d(text = '1 selected').click()
        d(text = 'Select all').click()
        u.setMenuOptions('Rotate right')
        # confirm back to gallery
        assert d(description = 'Switch to camera').wait.exists(timeout = 2000)

    # Testcase 27
    def testAddKeywordsToAllInGridView(self):
        """
        Summary: animate picture in gallery
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or video to select
        4.Tap select file dropdown 
        5.Tap select all option
        6.Tap extra menu
        7.Tap add keywords option
        8.Input tag and tap DONE icon
        9.Exit socialgallery app
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        d(text = '1 selected').click()
        d(text = 'Select all').click()
        # Step 6 + Step 7
        u.setMenuOptions('Add a keyword')
        # Step 8
        d(text="Enter new keyword").set_text("New Keyword")
        d.click(650,1130) # click 'done' icon on the keyboard.
        # confirm back to gallery
        self._longtouchscreencenter()
        d(text = '1 selected').click()
        d(text = 'Select all').click()       
        u.setMenuOptions('Add a keyword')
        assert d(text = 'New Keyword').exists

    # Testcase 28
    def testSlideshowAllInGridView(self):
        """
        Summary: Slideshow all in gallery
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or video to select
        4.Tap select file dropdown 
        5.Tap select all option
        6.Tap extra menu
        7.Tap Slideshow
        8.Random select a slide show mode
        """
        slideshow_option = random.choice(SLIDESHOW_OPTION)
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        d(text = '1 selected').click()
        d(text = 'Select all').click()
        # Step 6 + Step 7
        u.setMenuOptions('Slideshow')
        d(text = slideshow_option).click()
        time.sleep(3)
        # Since automation can't check this point, if it back to gridview treat it as pass.
        u.pressBack(1)
        assert d(description = 'Switch to camera').wait.exists(timeout = 2000)

    # Testcase 29
    def testAnimateToVideoAllInGridView(self):
        """
        Summary: Animate all in gallery
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or video to select
        4.Tap select file dropdown 
        5.Tap select all option
        6.Tap extra menu
        7.Tap Convert option
        8.Select the video convert settings
        9.Tap animate button
        10.Tap Save button
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        d(text = '1 selected').click()
        d(text = 'Select all').click()
        # Step 6 + Step 7
        u.setMenuOptions('Animate')
        d(text = 'Video').click()
        d(text = 'Create').click()
        time.sleep(20)
        d(text = 'Save').click.wait()
        time.sleep(2)
        # confirm create complete
        result = commands.getoutput('adb shell ls -l /sdcard/Sharing | grep mp4 | wc -l')
        if string.atoi(result) != 1:
            self.fail('animated failed')

    # Testcase 30
    def testAnimateToGIFAllInGridView(self):
        """
        Summary: Animate all in gallery
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or video to select
        4.Tap select file dropdown 
        5.Tap select all option
        6.Tap extra menu
        7.Tap Convert option
        8.Select the GIF convert settings
        9.Tap animate button
        10.Tap Save button
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        d(text = '1 selected').click()
        d(text = 'Select all').click()
        # Step 6 + Step 7
        u.setMenuOptions('Animate')
        d(text = 'Animated GIF').click()
        d(text = 'Create').click()
        time.sleep(2)
        d(text = 'Save').click.wait()
        time.sleep(2)
        # confirm create complete
        result = commands.getoutput('adb shell ls -l /sdcard/Sharing | grep gif | wc -l')
        if string.atoi(result) != 1:
            self.fail('animated failed')

    # Testcase 31
    def testDeselectAllInGridView(self):
        """
        Summary: Deselect all in gallery
        Step:
        1.Launch gallery activity 
        2.Enter Grid view
        3.Long touch a pic or video to select
        4.Tap select file dropdown 
        5.Tap select all option
        6.Tap select file dropdown
        7.Tap Deselect all option
        """
        # Step 3
        self._longtouchscreencenter()
        # Step 4 + Step 5
        d(text = '1 selected').click()
        d(text = 'Select all').click()
        # Step 6 + Step 7
        d(text = '20 selected').click()
        d(text = 'Deselect all').click()
        # Since automation can't check this point, if it back to gridview treat it as pass.
        assert d(description = 'Switch to camera').wait.exists(timeout = 2000)        

    def _longtouchscreencenter(self):
        time.sleep(2)
        d.swipe(350,700,351,701)
        time.sleep(2)

    def _setpictureas(self,option):
        if option == 'Wallpaper':
            d(text = 'com.intel.android.gallery3d').click()
        else:
            d(text = option).click()
