# Task # 2 – Web Page Design

## Source 1 - home page: https://www.louistoolkit.ca/

As far as I could find, this is the portal of the LOUIS system; dispite the main
function that allows users to login to their own profiles, these pages provide
very little information (to the subscribed users).

Most of the pages are well-designed, clear and obvious, so the changes I made
mainly focus on semantic consistency. Here they are:

1. since very limited information is served here, the web pages could be
   shrinked into one, with a "scrollspy" to manage all components (previously
   all pages).

2. due to the site serving as a portal to let users to login for further
   information, it makes sense that users focus on the login operation. So I
   changed the login panel to mask rest of the page by using **modal dialog**.

## Source 2: "Tools" page: URL not available

There is no such a "Tools" page. Instead, it contains 4 sub-topics. By putting
them into independent pages, the inner connections among them become a little
bit vague. so I chose **tabs** to represent them within the same "Tools"
component. In the case that such sub-topics have long phrases or there are too
many of such sub-topics, I would choose **list group** or **vertical navs**.

## Source 3: "Why LOUIS" page: https://www.louistoolkit.ca/whylouis/

This section has the similar issue to the above source. Meanwhile, what's
originally in "Why LOUIS?" and in "Comparison To Similar Tools" both talks the
same thing, however "Pricing" shows no advantage of LOUIS. So, my revision on
this is to change the first two into two tabs within the same component, while
Move the third one out.

There is no other current topics related to the pricing, however the purpose of
show price is to encourage people to subscribe it. So I created a new component
"Subscribe" to hold the original "Pricing" page as the first tab, and create a
new tab called "Subscribe" for further payment method entension.
