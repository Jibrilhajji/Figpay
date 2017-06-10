import { BrowserModule } from '@angular/platform-browser'
import { ErrorHandler, NgModule } from '@angular/core'
import { Http, HttpModule} from '@angular/http'

import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular'

import { CameraPreview } from '@ionic-native/camera-preview'
import { SplashScreen } from '@ionic-native/splash-screen'
import { StatusBar } from '@ionic-native/status-bar'

import { MyApp } from './app.component'

import { HomePage } from '../pages/home/home'
import { ApiProvider } from '../providers/api/api';

@NgModule({
  declarations: [
    MyApp,
    HomePage
  ],
  imports: [
    HttpModule,
    BrowserModule,
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage
  ],
  providers: [
    StatusBar,
    ApiProvider,
    SplashScreen,
    CameraPreview,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}
