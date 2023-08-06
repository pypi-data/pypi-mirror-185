# th2 gRPC generator template library (1.4.0)

This is the template project for creating custom gRPC libraries. It contains an example of proto messages and services. <br>
The tool generates code from `.proto` files and uploads built packages (`.proto` files and generated code) to the specified repositories.

## How to transform the template
1. Create a directory with the same name as the project name (use underscores instead of dashes) under `src/main/proto` directory (remove other files and directories if they exist).
2. Place your custom `.proto` files in the created directory. Pay attention to both the `package` specifier and to the `import` statements.
3. Edit `release_version` and `vcs_url` properties in `gradle.properties` file.
4. Edit `rootProject.name` variable in `settings.gradle` file. This will be the name of the Java package.
5. Edit `package_info.json` file in order to specify its name and its version for Python package (create the file in case it's absent).
6. Edit parameters of `setup.py` in `setup` function invocation such as: `author`, `author_email`, `url`. Do not edit the other's parameters.
7. Edit `README.md` file according to the new project.

Note that the name of the created directory under `src/main/proto` directory is used in Python (it's a package name).

## How to maintain a project
1. Perform the necessary changes.
2. Update the package version of Java in `gradle.properties` file.
3. Update the package version of Python in `package_info.json` file.
4. Commit everything.

## How to run project

### Java
If you wish to manually create and publish a package for Java, run the following command:
```
gradle --no-daemon clean build publish artifactoryPublish \
       -Purl=${URL} \ 
       -Puser=${USER} \
       -Ppassword=${PASSWORD}
```
`URL`, `USER` and `PASSWORD` are parameters for publishing.

### Python
If you wish to manually create and publish a package for Python:
1. Generate services with `Gradle`:
    ```
       gradle --no-daemon clean generateProto
    ```
    You can find the generated files by following path: `src/gen/main/services/python`
2. Generate code from `.proto` files and publish everything using `twine`:
    ```
    pip install -r requirements.txt
    pip install twine
    python setup.py generate
    python setup.py sdist
    twine upload --repository-url ${PYPI_REPOSITORY_URL} --username ${PYPI_USER} --password ${PYPI_PASSWORD} dist/*
    ```
    `PYPI_REPOSITORY_URL`, `PYPI_USER` and `PYPI_PASSWORD` are parameters for publishing.
   
## Release notes

### 1.4.0

+ Implement stubs creation for Python