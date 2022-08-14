import { Component, Input } from '@angular/core';
import {HttpClient,HttpEventType, HttpHeaders} from '@angular/common/http';
import { Subscription } from 'rxjs';
import { finalize } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'CSV Translator';
  @Input()
  fileName = '';
  uploadProgress:number;
  uploadSub: Subscription;
  constructor(private http: HttpClient) {}

    onFileSelected(event) {

        const file:File = event.target.files[0];
        
        if (file ) {
            this.fileName = file.name;
            const formData = new FormData();
            formData.append("file", file,file.name);
            console.log(file.size);
            let headers = new HttpHeaders();
            headers.append('file_name',file.name);
            const upload$ = this.http.post("http://127.0.0.1:5000/translate",formData,{
                reportProgress: true,
                observe: 'events',
                headers: headers
            }).pipe(finalize(() => this.reset()));
            console.log(upload$);
          this.uploadSub = upload$.subscribe(event => {
              if (event.type == HttpEventType.UploadProgress) {
                this.uploadProgress = Math.round(100 * (event.loaded / event.total!));
              }
            })
        }
    }
  cancelUpload() {
    this.uploadSub.unsubscribe();
    this.reset();
  }

  reset() {
    this.uploadProgress = null as any;
    this.uploadSub = null as any;
  }

}
