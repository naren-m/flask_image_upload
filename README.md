# flask_image_upload

Example on how to use flask to pass image as rest service

## Curl command sending image as payload

```sh
curl -F "filecomment=This is an image file" \
     -F "image=@newimage.jpg" \
     localhost:5000/upload
```

## Curl command to send json payload

```sh
curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:5000/post
```

## Start docker with code mounted

```sh
docker run -d --name flask -p 5000:5000 -v $PWD:/webapp narenm/flask:py3
```

## Reference

- [Camera with Rest Interface](http://blog.cudmore.io/post/2015/12/06/camera-with-a-rest-interface/)
- [Conda environment tutorial](http://www.naren.me/2017-02-28-Using-Anaconda-for-creating-virtual-environment/)
- [Conda docs](https://conda.io/docs/using/envs.html)
- [Flask video streaming](https://github.com/miguelgrinberg/flask-video-streaming)
- [REST API Http Requests for Humans with Flask](http://www.bogotobogo.com/python/python-REST-API-Http-Requests-for-Humans-with-Flask.php)
- [Building beautiful REST APIs using Flask, Swagger UI and Flask-RESTPlus](http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/)
- [Flask-Restful_S3_File_Upload.py](https://gist.github.com/RishabhVerma/7228939)
- [How-to-upload-a-file-to-the-server-in-flask-for-python](http://code.runnable.com/UiPcaBXaxGNYAAAL/how-to-upload-a-file-to-the-server-in-flask-for-python)
- [flask-uploads blog](http://www.patricksoftwareblog.com/tag/flask-uploads/)