
# Run Image
```bash
docker run
docker run -v path:mount #mount "path" from the local system at "mount" in the container
docker run --env env_variable #set environment variables in container
docker run -it #create interactive bash shell in container
docker run -p 127.0.0.1:80:8080 #publish port 8080 to host at port 80
docker run -p 80:80 #no host binding, accessible externally
```