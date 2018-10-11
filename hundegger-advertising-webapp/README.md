### What is this project about?

The resulting container includes a small [Flask](http://flask.pocoo.org/) webapp that shows pictures of machines manufactured by [Hundegger](https://www.hundegger.de). The photos are randomly selected from a given collection.

### What is the best way to start this container?

The following would be sufficient:
```
docker run -p 8888:5000 mijaec94/hundegger-advertising-webapp
```

This command is much smarter:
```
docker run -p 8888:5000 --name myContainer --rm mijaec94/hundegger-advertising-webapp
```

Afterwards the webapp should be available under: localhost:8888

### What additional technical information is available?

This projects includes a Dockerfile that creates an image with:

- python as a base-image
- flask installed inside
- a html template website
- some predefined urls that are randomly feeded into the render_template function

### Is this image already available on DockerHub?

Yes, it is available as mijaec94/hundegger-advertising-webapp!


### What else is there to know about?

This project was inspired by the [docker-curriculum](https://docker-curriculum.com/) and is intended exclusively for educational purposes!
