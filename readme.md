<!-- @format -->

## If using VS Code or other local based code editor for Stripe:

While stripe will work without a hitch if you get every bit of code correct without needing to
test it, you may still want to make sure that webhooks are working correctly. If using a "live"
IDE like gitpod then stripe will take your site as being "live" and therefore the webhooks can
be handled on their main site. What is different for VS Code and similar editors is that because
the website is only hosted locally, Stripe cannot send data over the internet to test it.

To work around this you have to install Stripe CLI on your computer. Below are the links to the
docs that will explain how to perform this action.

https://stripe.com/docs/stripe-cli
https://stripe.com/docs/stripe-vscode

Of course, VS Code does have an extension for Stripe as well. This inconjunction with Stripe CLI
will allow you to test Webhooks, trigger events, see them produced etc. Although I think working in
and env prevents VS Code from registering that Stripe CLI is downloaded. So it never worked for me.
The workaround I employed is running the process through the CMD. Below are instructions on how I
used Stripe CLI

1. Download the CLI
2. Unzip the file
3. Go the CMD and cd to where you downloaded it (This can be made easier by downloading the item
   Straight to the root of your files)
4. Run stripe.exe
5. Run stripe login
    1. You will be given a "key" for verification
    2. Press enter and login to the Stripe website when prompted
    3. Return back to the CMD
6. Run stripe listen --forward-to (your local domain e.g. http://127.0.0.1:8000)
    1. For it to work with this patricular project at the end of your domain add /checkout/wh
7. You will be given a secret key, use this in your site for STRIPE_WH_SECRET
    1. For this site I have my secret keys in an .env file located in the main projects folder with settings.py etc.
    2. You have to manually add this file, but it keeps your keys safe in production
    3. Also make sure to .gitignore .env files when using Github etc.
8. Once completed run your site
9. Open a seperate CMD, without closing the other one
10. Run stripe trigger <event>
    1. These events can be anything a user might do, to find all the events please see here: https://stripe.com/docs/cli/trigger
11. If all works you will be presented with a status code in the editors terminal and also the first CMD
12. This will confirm whether or not Stripe Webhooks is working as intended or not
