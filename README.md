# WebcamSettingsModule
<p> The webcam settings module is a tool created for developers to set up various settings components like volume or brightness. These components are displayed on the screen for users to adjust. This is especially useful in situations where the user doesn't have an interface for changing controls (like in a Raspberry Pi project with no peripherals) but does have a camera available. </p>
<br>


![Structure](images/Structure.drawio.png)


<h1> Usage </h1>
<h2> General </h2>
<p>The user can navigate through the menu using their index tip as a pointer, as well as through gesture recognition for some parts of the menu. The pointer is indicated by the green-circle at the tip of the index finger.</p>

<ol>
 <li> 
  <h2> Main Menu </h2>
  <p> When the webcam recognition function is activated, the user will be presented with the default menu screen. The available submenus are in the top-left of the screen, the settings component are at the bottom and the exit button is in the top-right.</p> 
 </li>

  <li> 
   <h2> Submenu Navigation </h2>
   <p> Users can navigate through the submenus by pointing at the top-left of the screen. Submenus consist of different groups of components. Depending on the number of settings, the program may only have one submenu and hence submenu navigation may not be required. </p>
 </li>
 
  <li> 
   <h2> Adjusting Settings </h2>
   <p> The user can then adjust the settings depending upon the particular component. For slider-bars, users can drag or point to the desired value level while in toggle components, users can simply point to the location of the desired value. Once the user is satisfied with the change, they must use a thumbs-up gesture to return to the submenu.
 </li>
 
  <li>
   <h2> Exiting the Settings </h2>
   <p> To exit the settings, the user simply has to point to the top-left of the screen. </p>
 </li>
  
</ol>
