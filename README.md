# python_key_value

1. <b>How to install or build the software                                  </b>
2. <b>How to start the server                                               </b>
3. <b>How can we try the server and see that it is working                  </b>   
4. <b>How to run the tests                                                  </b>    
5. <b>Have background information about technical decisions is a plus       </b>

## 1. How to install or build the software
Well, just grab python, and then the dependencies with pip
grabbing python is relatively easy on Linux distributions since its built-in.
Windows and Mac installers can be found at https://www.python.org/downloads

Once you are done, you can verify you are done by running the command:
```$ python --version```

The output should be something like:

```>>> Python 3.10.5```

Next, you should navigate to the repository's root directory, where the file: **requirements.txt** is.

Now there is a choice to make:

**Contain our stuff in an environment**, or just mess up our python with the dependency of every project we ever try to run?

So, let's use venv for that. It should be a built-in python module but if it's not, you can just use:
```$ python -m pip install venv ```

Next to have our application's dependencies contained and separate from our base python:
``` $ python -m venv env```

A virtual environment should be created and ready for use.

On Linux you should run the following which will activate the environment:
```$ source bin/activate```

Next, we will install our dependencies **into the environment, we just created and activated**:
```$ pip install -r requirements.txt```


## 2. How to start the server

From the root directory you should:
```$ cd app```
```$ python -m flask run```

## 3. How can we try the server and see that it is working
The address that is visible on the console after running
```$ python -m flask run```
by default it should be **127.0.0.1:5000** or **localhost:5000**
This is where the service is available at. You should type this into your address bar in a browser like Brave, Mozilla or Chrome. From then on it will be pretty self-explanatory.

## 4. How to run the tests

in the repository root, use the following command:
```$ pytest```

## 5. Have background information about technical decisions is a plus

Okay, I will tell you what technology I chose and why.

So for a server/backend solution I went with **Flask**. It's lightweight and simple, I guess it was just alright for my needs. Also I haven't really used it for quite some time now, and I wanted to. My other idea was to go with Django, but I felt like that's like using a sledgehammer to crack a nut.

However since I've already mentioned Django, it's a perfect time to talk about why I used **Peewee ORM**. Again, very much like Flask it's small and simple. However it has a lot of the benefits of the Django ORM which is something that I'm used to and I quite frankly like it. This was actually the firs time I used Peewee, and I enjoyed it very much.

While it came with Flask, I actually wanted to stay with **Jinja2** for templating, as it's simple, great fit for my goals and quite well known for the average Django user.

I think **pytest** is a great tool for testing applications, I like how out of the box pytest is.

<br>
Code-wise I'd only like to explain 3 things.

1. Adding and getting keys and values are done with blueprints, which then get registered into the application. The reason behind this is simple, I like to keep a clean house - so to say. Different functionalities should reside in different files. That is just how it should be.
2. There are handlers. I decided to create the handlers for 2 reasons. Testing my functionality is easier this way, and I could also introduce an interface-like class that just warms my heart, really.
3. I didn't test much, because I.... well, I wasted a lot of time and didn't have any left...