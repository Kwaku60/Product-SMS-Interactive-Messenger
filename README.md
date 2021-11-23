# Running Application lcoally

# installation

pipenv shell
pipenv install
$python
from app import db
db.create_all()

# running

navigate to the api directory:
python run.py

navigate to the app directory:
npm install
npm start

# Running Application on Docker

docker-compose build
docker-compose up

Note: Need to get the db created in docker, ran into issues, appliations serves, but endpoints fail in docker environment as a result.

#####

# Reflection (post development):

# context/my background

I haven't used Flask or SQLAlchemy before. I'm familiar with python, though in the context of algorithms, datastructures, and some lambdas in AWS- so I haven't built a full stack app with the language until this project. I've used react before, though I've been building production angular the last year, so jumping back into it I wanted to only use functional components for a more modern approach, so briefly looked at some documentation.

# process

1. Spent some time reading documentation and studying code to get a base for python and flask development. Did the same/refreshed for react. Also learned about Flask html. I spent about 2 hours here in the research stage.
2. Next I spent about 45 minutes mapping out a solution, my approach, the structure, and the design of the application. I prefer to clearly state a solution- before jumping in, so I can stay on track and retrace steps more methodically instead of wasting time guessing or losing progress when returning (or in a team context, passing a project off) by poor process tracking.
3. I spent about 3.5 hrs developing. I wanted to cap at the 5 hours, but I was determined to get past the things that blocked me along the way (the CORS issue with react making requests to the python backend, the app running locally but running into import issues and missing packages once built on docker)
4. I was able to get the python backend set up relatively quickly. I tested all of my endpoints with postman, and had success with the twilio api. I think most of my issues came with connecting front and backend and hosting on docker( which was also new to me).
5. When I encountered the cors issue with React, I pivoted to a flask html front end (I left the extra files in here just for development refference). Though, I had a moment of clarity, and discovered a work around for CORS and returned to my original react plan, though had little time left at this point.
6. After discovering proper use of the requirements.txt file, I was able to get everything hosted on Docker succesfully. However, I had trouble getting the database started. I tried a few approaches and looked up some flask examples, yet the db wouldn't start, so my fetches were failing within docker. So the app functions locally, though there's trouble when hosted on docker..

# with more time

I would have certainly made my python files more modular, broken down my react components, made functions less repetitive. After figuring out the db hosting on docker, the biggest thing would be adding style to the front end. I was overtime, so I figured I'd focus on basic functionality but it would have been nice to organzie layout and have some style themes for each component and to toggle some of that with state changes...

Overall, I had a really great time learning some new technologies and building for the first time with some of them. Really excited about this stack and hoping to have more opportunities to learn fast, challenge myself and keep growing. Thank you!

######

######

######

# Introduction:

Thanks for continuing your application to Postscript Engineering!

This assignment very closely mimics work we are doing at Postscript - it’s a stripped down version of a core part of our functionality. So it should give you a good sense of whether you want to work at Postscript, and give us a good sense of what it would be like to have you on our team.

In particular, to do well on this project you’ll probably need to work like we do: follow the [80/20 rule](https://en.wikipedia.org/wiki/Pareto_principle). There are a lot of technologies listed below and we want you to use all of them. You’re probably not familiar with all of them, but you only need to learn enough to get the assignment working. We’re not looking for perfect usage of any tool.

In addition to the code, please send us: 1) an explanation of your solution, 2) a list of the technologies used that were totally new to you, so we can take that into account, 3) roughly how long you took

## Evaluation Criteria:

- Learning & implementing new frameworks / languages
- Speed / Resourcefulness
- Working within a broad spec / autonomous decision making
- Quality given the amount of time taken (it would be reasonable to submit a medium-quality solution that you were able to do quickly)

## Assignment:

Please create a tool that can send shipment notifications as text messages. All of the functionality you create must be exposed through a single front-end interface. It must interact with back-end API’s to perform its functions.

The main flows to implement are:

- A user can choose a particular product and save a draft of a shipping notification for that product. For purposes of this assignment, we want to be able to create different shipping notifications for different products. There can be multiple draft message for a product or one per product, that is up to you.

- A user can also look up draft versions of these text messages that have been saved, and click a button to actually send one of them to a number (which they provide at the time of sending).

Additional details under “User Flows.”

## Tooling:

Please use the following technologies. If you are unfamiliar with them, learn the minimum required to get the job done. When you send in your assignment, you can tell us which ones you had to learn from scratch and we will take that into account.

- Flask (Python) to create the API endpoints
- Connect to DB using SQLAlchemy or pure SQL
- PostgreSQL database
- ReactJS Front-end (or Flask HTML)
- It is totally fine to use only pure HTML (via Flask) if you are unfamiliar with front-end technologies. There is room on our team for pure backend developers. But if you have front-end skills you can show them here.
- Twilio to send text messages (if for some reason you can’t create a trial account for free credit, let us know)

This does not need to be deployed and available to the internet as long as it can be run locally. The assignment should utilize Docker Compose in order to run locally on any setup.

## User Flows:

- Users should be able to query a list of available products
- Users should be able to create and save a message for a product
- Saving a message requires a product_id to be attached to the message and should throw an error otherwise
  For example, the message object might look like

```
{
  "message" : "Some string",
  "Product_id":1
}
```

- Users should be able to view messages for a product
- Users should be able to send messages for a product

- This should utilize the Twilio API -- use a Twilio trial account, it is OK if the message does not send to outside / non-whitelisted numbers.

## Getting Setup:

There are 2 folders contained with this homework:

**`api`**

The `api` folder houses the `Dockerfile` to build and run the `Flask` application against the `db`. It contains a bootstrapped `Flask` object and `Flask-SQLAlchemy` already setup to work with the larger `docker-compose.yml` file of this homework.

**`app`**

The `app` folder contains a boilerplate `react-scripts` react app with no additional functionality. Feel free to replace this with your technology of choice (and appropriately update the `Dockerfile` and/or the `docker-compose.yml` file if need-be).

**Note:** If you'd like to use `yarn` instead of `npm`, open the `app/Dockerfile` and swap `npm install --silent` with `yarn install --silent`

### Running the Environment

Once you've created a `package.json` in the `app` folder, you're ready to run the `docker-compose` environment.

By default, when running the `docker-compose` of this repo, the ports will map as follows:

- `api` - Port 5000
- `db` - Port 5432
- `app` - Port 3000

Running the environment is now as easy as `docker compose up`.

- Visit `http://localhost:5000/health-check` to verify the api is working.
- Visit `http://localhost:3000` to see your frontend application

## Delivery:

Please do not spend more than 5 hours on this assignment.

We recommend using git archive; we want a zip without commits.

Please deliver the assignment in a zip file and submit it through the Greenhouse link provided.
