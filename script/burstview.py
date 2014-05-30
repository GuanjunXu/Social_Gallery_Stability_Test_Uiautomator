#!/usr/bin/python
# coding:utf-8

from uiautomatorplug.android import device as d
import commands
import re
import subprocess
import os
import string
import time
import sys
import util 
import unittest


u=util.Util()
#Written by Piao chengguo

# PATH
STORAGE = 'adb shell ls -l /storage/sdcard0/Sharing/ | grep '
ANDROFOLDER ='adb shell ls -l /sdcard/DCIM/100ANDRO/ | grep '


# key

#################################
PACKAGE_NAME = 'com.intel.android.gallery3d'
ACTIVITY_NAME = PACKAGE_NAME + '.app.Gallery'

class GalleryTest(unittest.TestCase):
    def setUp(self):
        super(GalleryTest,self).setUp()
        #Add on May 26th due to device always reboot by itself
        if d(text = 'Charged').wait.exists:
            commands.getoutput('adb root')
            time.sleep(5)
            commands.getoutput('adb remount')
            d.swipe(360,980,719,980)
        u._clearAllResource()
        u._checkBurstResource()
        u.launchGallery()
        self._enterBurstView()


   

    def tearDown(self):
        super(GalleryTest,self).tearDown()
        self._pressBack(4)
        u._clearAllResource()
        time.sleep(2)
########################################################

# Test case 1
    def testSmallPlayBurstIconOfDissolve(self):
        """
        Summary:This case test play burst with Dissolve mode in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap small play burst icon -> Dissolve, wait some seconds to check if stopped the playing
        """  
        #Step 2
        #Tap small play burst icon twice,the fist tap try to activity the tool bar due to it is disappeared
        self._burstMenuOption('Playback','Dissolve')
        time.sleep(7)
        d.click(324,100)
        time.sleep(1)
        assert d(resourceId = 'com.intel.android.gallery3d:id/action_share').wait.exists(timeout = 3000), 'play fail'

# Test case 2    
    def testSmallPlayBurstIconOfFlash(self):
        """
        Summary:This case test play burst with Flash mode in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap small play burst icon -> Flash, wait some seconds to check if stopped the playing
        """  
        self._burstMenuOption('Playback','Flash')
        time.sleep(7)
        d.click(324,100)
        time.sleep(1)
        assert d(resourceId = 'com.intel.android.gallery3d:id/action_share').wait.exists(timeout = 3000), 'play fail'

# Test case3
    def testSmallPlayBurstIconOfPageflip(self):
        """
        Summary:This case test play burst with Page flip mode in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap small play burst icon -> Page flip, wait some seconds to check if stopped the playing
        """ 
        self._burstMenuOption('Playback','Page flip')
        time.sleep(15)
        d.click(324,100)
        time.sleep(1)
        assert d(resourceId = 'com.intel.android.gallery3d:id/action_share').wait.exists(timeout = 3000), 'play fail'
# Test case 4
    
    def testDeleteBurstPics(self):
        """
        Summary:This case test delete burst pictures in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap trash icon -> delete,wait some seconds
          3. Get current burst picture count
          4. Verify if delete successful
        """  
        resultNO1 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        self._burstMenuOption('Delete','Delete')
        time.sleep(1)
        resultNO2 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        time.sleep(1)
        if resultNO1 == resultNO2:
            self.fail('delete BST picture fail')
    
# Test case 5
    def testMenuKeyOfRotateLeft(self):
        """
        Summary:This case test rotate left burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> Rotate left,check Rotate left progress pops up.
        """  
        self._burstMenuOption('Rotate left')
        d.expect('burstview.png')

# Test case 6
    def testMenuKeyOfRotateRight(self):
        """
        Summary:This case test rotate right burst pictures by menu key in burst view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> Rotate right,check Rotate right progress pops up.
        """  
        self._burstMenuOption('Rotate right')
        d.expect('burstview.png')

# Test case 7
    def testMenuKeyOfSync(self):
        """
        Summary:This case test sync pictures via menu key
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> Rotate left,check Rotate left progress pops up.
        """  
        d.press('menu')
        assert d(text = 'Social Sync').wait.exists(timeout = 3000), 'unable to find sync icon'
       
     
# Test case 8
    def testMenuKeyOfConvert(self):
        """
        Summary:This case test convert pictures via menu key
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> convert -> animated - > convert -> save,check Rotate left progress pops up.
        """  
        resultNO1 = commands.getoutput(STORAGE +'gif' + ' | wc -l')
        self._burstMenuOption('Animate','Animated GIF','Create')
        assert d(text = 'Save').wait.exists(timeout =5000), 'add tag fail' 
        d(text = 'Save').click.wait()
        resultNO2 = commands.getoutput(STORAGE +'gif' + ' | wc -l')
        if resultNO1 == resultNO2:
            self.fail('delete BST picture fail')


# Test csae 9
    def testAddVenue(self):
        """
        Summary:This case test add venue
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> setting bar
        """  
        self._addKeyWordEventVenue('venue',"kaihui") 
        time.sleep(1)
        assert d(text = 'kaihui').wait.exists(timeout =2000),'add venue fail' 

# Test case 10
    def testAddEvent(self):
        """
        Summary:This case test add event
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> setting bar
        """  
        self._addKeyWordEventVenue('event',"shangban")
        time.sleep(1)
        assert d(text = 'shangban').wait.exists(timeout =2000),'add event fail' 

# Test case 11
    def testAddKeyword(self):
        """
        Summary:This case test add keyword
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> setting bar -> add keyword
        """  
        self._addKeyWordEventVenue('Keyword',"test123")
        time.sleep(1)   
        assert d(text = 'test123').wait.exists(timeout =2000),'add tag fail'  

# Test case 12
    def testCheckDetails(self):
        """
        Summary:This case test check details
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap menu -> Details
        """ 
        self._burstMenuOption('Details')
        assert d(resourceId='com.intel.android.gallery3d:id/facebook_icon').wait.exists(timeout =2000),'verify detail fail' 

# Test case 13
    def testSmallPlayBurstIconOfDissolveInEditView(self):
        """
        Summary:This case test paly burst pictures with Dissolve in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon -> Select all -> play burst icon -> Dissolve,wait some seconds.(Can not check during playing)
        """ 
        self._SlideShowIconEditScreen('Dissolve')
        time.sleep(5)
        assert d(className = 'android.widget.TextView').wait.exists(timeout =2000),'play BST file fail' 

# Test case 14
    def testSmallPlayBurstIconOfFlashInEditView(self):
        """
        Summary:This case test paly burst pictures with Flash in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon -> Select all -> play burst icon -> Flash,wait some seconds.(Can not check during playing)
        """          
        self._SlideShowIconEditScreen('Flash')
        time.sleep(5)
        assert d(className = 'android.widget.TextView').wait.exists(timeout =2000),'play BST file fail'          

# Test case 15
    def testSmallPlayBurstIconOfPageflipInEditView(self):
        """
        Summary:This case test paly burst pictures with Page flip in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon -> Select all -> play burst icon -> Page flip,wait some seconds.(Can not check during playing)
        """         
        self._SlideShowIconEditScreen('Page flip')
        time.sleep(15)
        assert d(className = 'android.widget.TextView').wait.exists(timeout =3000),'play BST file fail'          

# Test case 16
    def testRandomSelBusrtPicsExportToGalleryInEditView(self):
        """
        Summary:This case test random select some burst pictures export to gallery in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon twice to enter burst edit view
          3. Get random generated a number and related (x,y) coordinate
          4. Choose the selected pictures -> extra menu icon -> Export to gallery
          5. Check if export to gallery successful
        """ 
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        u.selectPictueWhenEditBurst(3)
        resultNO1 = commands.getoutput(ANDROFOLDER + 'jpg' + ' | wc -l')        
        self._burstMenuOption('Export to gallery')
        resultNO2 = commands.getoutput(ANDROFOLDER + 'jpg' + ' | wc -l')   
        if resultNO1 == resultNO2:
            self.fail('delete BST picture fail')



# Test case 17
    def testSelectAllBusrtPicsExportToGalleryInEditView(self):
        """
        Summary:This case test select all burst pictures export to gallery in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Get the burst picture count before export to gallery
          2. Launch Intel gallery and enter to burst view
          3. Tap edit burst icon twice to enter burst edit view, then select all -> extra menu icon -> Export to gallery, wait some seconds
          4. Get the NOT burt picture count after export to gallery
          5. Check if export to gallery successful
        """ 
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        time.sleep(1)
        d(resourceId = 'com.intel.android.gallery3d:id/selection_menu').click.wait()
        d(text = 'Select all').click.wait()
        resultNO1 = commands.getoutput(ANDROFOLDER + 'jpg' + ' | wc -l') 
        self._burstMenuOption('Export to gallery')
        time.sleep(1)
        resultNO2 = commands.getoutput(ANDROFOLDER + 'jpg' + ' | wc -l') 
        if resultNO1 == resultNO2:
            self.fail('Export picture fail')
#Test case 18
    def testRandomSelBusrtPicsDeleteMarkedInEditView(self):
        """
        Summary:This case test random select some burst pictures delete marked in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Get the burst picture count before delete marked
          2. Launch Intel gallery and enter to burst view
          3. Tap edit burst icon twice to enter burst edit view
          4. Get random generated a number and related (x,y) coordinate
          5. Choose the selected pictures -> extra menu icon -> delete marked 
          6. Check if delete marked successful
        """ 
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        u.selectPictueWhenEditBurst(3)
        resultNO1 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')                 
        self._burstMenuOption('Delete marked')
        resultNO2 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        if resultNO1 == resultNO2:
            self.fail('Export BST picture fail')

# Test case 19
    def testSelectAllBusrtPicsDeleteMarkedInEditView(self):
        """
        Summary:This case test select all burst pictures delete marked in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon twice to enter burst edit view, then select all -> extra menu icon -> delete marked, wait some seconds
          3. Verify the test result
        """  
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        time.sleep(1)
        d(resourceId = 'com.intel.android.gallery3d:id/selection_menu').click.wait()
        d(text = 'Select all').click.wait()
        resultNO1 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        self._burstMenuOption('Delete marked')
        time.sleep(1)
        resultNO2 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        if resultNO1 == resultNO2:
            self.fail('delete marked fail')

# Test case 20
    def testRandomSelBusrtPicsDeleteUnMarkedInEditView(self):
        """
        Summary:This case test random select some burst pictures delete unmarked in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Get the burst picture count before delete unmarked
          2. Launch Intel gallery and enter to burst view
          3. Tap edit burst icon twice to enter burst edit view
          4. Get random generated a number and related (x,y) coordinate
          5. Choose the selected pictures -> extra menu icon -> delete unmarked
          6. Check if delete unmarked successful
        """ 
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        time.sleep(1)
        d(resourceId = 'com.intel.android.gallery3d:id/selection_menu').click.wait()
        u.selectPictueWhenEditBurst(3)
        resultNO1 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        self._burstMenuOption('Delete unmarked')
        time.sleep(1)
        resultNO2 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        if resultNO1 == resultNO2:
            self.fail('delete marked fail')
    
# Test case 21
    def testSelectAllBusrtPicsDeleteUnMarkedInEditView(self):
        """
        Summary:This case test select all burst pictures export to gallery in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Get the burst pictures count before delete unmarked
          2. Launch Intel gallery and enter to burst view
          3. Tap edit burst icon twice to enter burst edit view, then select all -> extra menu icon -> delete unmarked, wait some seconds
          4. Get the burt pictures count after delete unmarked
          5. Check if delete unmarked successful
        """         
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        time.sleep(1)
        d(resourceId = 'com.intel.android.gallery3d:id/selection_menu').click.wait()
        d(text = 'Select all').click.wait()
        resultNO1 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        self._burstMenuOption('Delete unmarked')
        time.sleep(1)
        resultNO2 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        if resultNO1 != resultNO2:
            self.fail('delete unmarked fail')

# Test case 22
    def testPlayBurstPictures(self):
        """
        Steps:
             1.Launch gallery activity 
             2.Enter Full View
             3.Tap play burst icon
        """
        d.click(350,620)  
        time.sleep(7)
        d.click(324,100)
        time.sleep(1)
        assert d(resourceId = 'android:id/home').wait.exists(timeout=2000),'play fail '

# Test case 23
    def testDeleteBusrtPicsInEditView(self):
        """
        Summary:This case test delete burst pictures in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1. Launch Intel gallery and enter to burst view
          2. Tap edit burst icon twice to enter burst edit view, then tap extra menu icon -> delete burst, wait some seconds
          3. Get the burst pictures after delete burst and check the result
        """  
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        time.sleep(1)
        d(resourceId = 'com.intel.android.gallery3d:id/selection_menu').click.wait()
        d(text = 'Select all').click.wait()
        resultNO1 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        self._burstMenuOption('Delete burst')
        time.sleep(1)
        resultNO2 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        if resultNO1 == resultNO2:
            self.fail('delete burst fail')

# Test case 24
    def testRandomSelectBusrtPicsConvertInEditView(self):
        """
        Summary:This case test random select some burst pictures convert in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
             1.Launch gallery activity 
             2.Enter Burst Edit View
             3.Radom select some  pics
             4.Tap extra menu icon
             5.Tap animate option
        """
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        u.selectPictueWhenEditBurst(3)
        resultNO1 = commands.getoutput(STORAGE + 'gif' + ' | wc -l')        
        self._burstMenuOption('Animate marked','Animated GIF','Create')
        time.sleep(3)
        assert d(text = 'Save').wait.exists(timeout =3000),'add tag fail' 
        d(text = 'Save').click.wait()
        resultNO2 = commands.getoutput(STORAGE + 'gif' + ' | wc -l') 
        if resultNO1 == resultNO2:
            self.fail('Create BST picture fail')  



# Test case 25
    def testSelectAllBusrtPicsConvertInEditView(self):
        """
        Summary:This case test select all burst pictures export to gallery in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
          1.Launch gallery activity 
          2.Enter Burst Edit View
          3.Select all pictures
          4.Tap extra menu icon
          5.Tap animate option
        """ 
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        time.sleep(1)
        d(resourceId = 'com.intel.android.gallery3d:id/selection_menu').click.wait()
        resultNO1 = commands.getoutput(STORAGE + 'gif' + ' | wc -l') 
        d(text = 'Select all').click.wait()     
        self._burstMenuOption('Animate marked','Animated GIF','Create')
        time.sleep(3)
        assert d(text = 'Save').wait.exists(timeout =3000),'create picture fail' 
        d(text = 'Save').click.wait()
        resultNO2 = commands.getoutput(STORAGE + 'gif' + ' | wc -l') 
        if resultNO1 == resultNO2:
            self.fail('Create BST picture fail')        


# Test case 26
    def testSelectDeselectBurstPicsInEditView(self):
        """
        Summary:This case test select and deselect pictures in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
              1.Launch gallery activity 
              2.Enter Burst Edit View
              3.Tap select option in actionbar
              4.Select select all option 
              5.Tap select option in action bar
              6.Select deselect all option 
              7.Exit social gallery app
        """
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        time.sleep(1)        
        d(text ='0 selected').click.wait()
        d(text = 'Select all').click.wait()
        time.sleep(1)
        d(resourceId ='com.intel.android.gallery3d:id/selection_menu').click.wait()        
        d(text = 'Deselect all').click.wait()
        time.sleep(1)
        assert d(text = '0 selected').wait.exists(timeout=1000),'Deselect fail'

 # Test case 27       
    def testMarkUnmarkBurstPicsInEditView(self):
        """
        Summary:This case test mark and unmark pictures in burst edit view.
        Precondition: There are burst pictures in sdcard
        Steps:
             1.Launch gallery activity 
             2.Enter Burst Edit View
             3.Mark 3 pictures via tap checkbox and check the selected number is correct
             4.Unmark 2 pictures via tap checkbox and check the selected number is correct
             5.Exit social gallery app
        """
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        u.selectPictueWhenEditBurst(3)
        u.selectPictueWhenEditBurst(2)
        resultNO1 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        self._burstMenuOption('Delete burst')
        time.sleep(1)
        resultNO2 = commands.getoutput(ANDROFOLDER + 'BST' + ' | wc -l')
        if resultNO1 == resultNO2:
            self.fail('delete burst fail')

# Test case 28        
    def testTouchCheckMarkIcon(self):
        """
        Summary:This case test touch check mark icon back to upper level.
        Precondition: There are burst pictures in sdcard
        Steps:
             1.Launch gallery activity 
             2.Enter Burst Edit View
             3.Tap Checkmark Icon
             4.Exit social gallery app
        """ 
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        u.selectPictueWhenEditBurst(3)
        assert d(text = '3 selected').wait.exists(timeout =3000),'tap mark fail'        





######################################################################################################################
    def _enterBurstView(self):
        '''
        Enter the burst view...
        '''  
        time.sleep(1)
        #d.expect('100ANDRO.png')
        d.click(370,720)
        time.sleep(1)
        #d.expect('burst.png')
        d.click(350,660)
        time.sleep(2)
        #d.expect('burstview.png')
        d.click(324,100)
        #d.expect('GalleryBST.png')
        time.sleep(1)
    
   
    ########################################
    def _burstMenuOption(self,selection,option=None,button=None):
        d(className = 'android.widget.ImageButton').click.wait()
        time.sleep(1)
        d(text = selection).click.wait()
        time.sleep(1)
        if option == None :
          pass
        else:
          d(text = option).click.wait()
        if button == None:
          pass
        else:
          d(text = button).click.wait()
        time.sleep(3)   
 

    def _addKeyWordEventVenue(self,word,text):
        self._burstMenuOption('Details')     
        if word == 'Keyword' :
            time.sleep(1)
            d().swipe.up()
            time.sleep(2)  
            d(resourceId='com.intel.android.gallery3d:id/add'+ word + 'Button').click.wait()
            time.sleep(1)
            d(text ="Enter new keyword").set_text(text)
            time.sleep(1)                  
        else:
            time.sleep(1)  
            d(resourceId='com.intel.android.gallery3d:id/'+ word +'_edit').click.wait()
            time.sleep(1)
            d(text ="Enter new " + word).set_text(text)
            time.sleep(1)
        d.click(656,1130)



    def _SlideShowIconEditScreen(self,status):
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_burst').click.wait()
        time.sleep(1)
        d(resourceId = 'com.intel.android.gallery3d:id/selection_menu').click.wait()
        d(text = 'Select all').click.wait()
        d(className = 'android.widget.TextView').click.wait()
        d(text = status).click.wait()
        time.sleep(7) 
   

###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
   
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#



    def _pressBack(self,touchtimes):
        for i in range(1,touchtimes+1):
            d.press('back')         
