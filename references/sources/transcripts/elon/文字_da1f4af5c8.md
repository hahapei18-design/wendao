# Tesla (TSLA) Q2 2018 Earnings Conference Call Transcript

- 人物: elon
- 视频编号: 文字_da1f4af5c8
- 频道: 文字稿
- 日期: 2018-08-06
- 分类: earnings_call
- 链接: https://www.fool.com/earnings/call-transcripts/2018/08/06/tesla-tsla-q2-2018-earnings-conference-call-transc.aspx
- 来源: 网站整理的文字稿(Professional transcript, Musk's lines only),只含本人发言,原稿无时间戳

---

Hi. Thank you for joining. First of all, I'd like to say we're incredibly proud of the Tesla team for producing 7,000 Model 3, Model S, and Model X vehicles in the last week of June. It was an amazing effort. It's an honor to work with such a great team to produce that incredible result. It's like mind-blowing. We continued to achieve 5,000 Model 3s per week, or 7,000 combined S, X, and 3, multiple weeks in July, showing that, so we're able to do this on a sustained basis. And we expect to, in the absence of a force majeure or some very unexpected event, be able to achieve an average of 5,000 Model 3s or above for Q3 and 2,000 Model S, Xs or above per week for Q3 as well. So essentially, 7,000 cars a week-plus on average for Q3. That's an amazing jump from only a year ago. We were producing 2,000 vehicles a week. It's really kind of a mind-blowing leap forward for a manufacturing company. So, yeah, just incredible work by the team to do that. Many, many late nights, weekends, extreme amounts of effort and lots of smart ideas. It's amazing. One of the results you're seeing is that the Model 3 market share has surpassed all competitor premium midsized sedans combined. So Model 3 market share is now a majority, in July, it was a majority of all premium sedans. That trend is, we think, likely to continue. We do not think it will stop there. I have Robin Ren here, who is our worldwide head of sales, to talk about some of the interesting elements that we're seeing in terms of cars that people are trading in, the sales and demand trends. It's looking really positive. We're also getting great feedback on Model 3 from our customers, and we're now delivering the performance, dual-motor, and all-wheel-drive versions, and the Model 3 reviews are outstanding. Really couldn't ask for better reviews from some of the toughest critics in the world. Yeah, the thing that we're really proud of is that the more Model 3s we deliver to the field, it's actually causing parallel growth of our sales. So, we deliver a Model 3 to somebody, they love it, they tell all their friends. Really our customers are our primary sales force. They love their car and take their friends for a drive and that's the thing that fundamentally drives our sales, but not everyone has a brand-new [Inaudible] Model 3 obviously, so we need to get the cars out there for test drives. As it is right now, not even all stores in North America have Model 3 for test drives. We prioritize getting cars to customers but we're soon going to have Model 3s available for test drives in all stores in both the performance version and the rear-wheel-drive version. So because a lot of people, they will not buy a car until they test drive it, which is not unreasonable. Although on Sunday when I delivered a -- we're testing out like direct delivery, which I think is definitely the future, direct delivery from factory to customer's home or work or wherever they are -- the guy who bought it had never actually even sat in a Model 3. I was like, "Wow, OK." I asked him, "Well, how do you feel about the car now that you have it and you've driven it?" He's like, "I love it. It's amazing." So, yes. It seems to be really well-received. So, at a production rate of 7,000 cars a week, we believe we can be sustainably profitable from Q3 onwards. We're going to try to raise that rate of the Model 3 production steadily in the coming quarters and try to get to the 10,000-cars-a-week number as soon as we can. As we spent a lot of time debugging a wide range of manufacturing issues that the potential for our existing lines to be able to produce far more cars is much greater than expected. That by simplifying production lines, by speeding them up, by, in some cases, everything's being done manual instead of automatic, and in other cases, having be done automatic instead of manual, we've been able to achieve dramatic improvements to the output of existing lines, which means that our capex growing from 5,000 cars a week to 10,000 cars a week is a tiny fraction [Inaudible]. Capex growing from 5,000 to 10,000 is a tiny fraction of the capex needed to grow from 0 to 5,000 Model 3s. This is, I think, very good news for capital efficiency of the company. And with [Inaudible], that it's going to inform future mass market vehicles that we produce. And from an operating-plant standpoint, from Q3 onwards, I really want to emphasize our goal is to be profitable and cash-flow positive for every quarter, going forward. Now obviously, if there's a big recession or there's a severe force majeure event that interrupts the supply chain, that's not always possible but we're confident that in, provided the economy is roughly where it is today or reasonably good and there's not a big force majeure event that I feel comfortable achieving a GAAP income positive and cash-flow positive quarter every quarter from here on out. There may be occasional quarters, where we pay back a big loan or something, where there may be just because we paid back a big loan but absent that, it would be cash-flow positive. So, once again, I want to thank the Tesla team for their incredible work and our customers for their support. Without the great people we have at Tesla and the customers who put their faith in us by buying our product, we would not be here today and, yeah, really never been more excited about the future of Tesla. We've got super exciting set of products to bring out in the future. And, yeah, I mean, sorry if I sound a little tired. I've been working like crazy in the body shop lately but it's really going great, super excited. It's like, yeah, some good people. And a number of the executive team here, [Inaudible] asked the three key leaders of the Tesla autopilot team to be here. So, I think to go from here to see if autopilot leaders of Tesla could introduce themselves and say a bit about what you're working on, what you're excited about in the future. Sorry if I put you guys on the spot or anything. I think we're making pretty radical advances in the core software technology and the division beyond that. And then very importantly with the Tesla self-driving chip technology that we've been working on for three years is finally coming to fruition. Pete Bannon is going to talk a lot about that but it's a plug-in replacement for the existing computer and enables an order of magnitude improvements in operations per second or frames per second as a way to think about it. And we think this is really the key to Tesla full vehicle autonomy. And [Inaudible] easy to replace. I'll let Pete talk about that. So, let me start off like Stuart, Andrej, and then Pete.

You need to talk louder, by the way.

Integrated navigation. So, you'd like [Inaudible] by the way, a little tip for if you're driving Model S or X or 3, is if you just tap the Navigate button and just drag down, it will automatically navigate you to your home or work, depending upon where you are. That's a pretty cool feature.

Yeah, actually, Pete, maybe just [Inaudible] know about your background but not everyone does. So if you could just like ... Pete's a super humble guy but it would be great just to talk about the stuff you've done before.

Yeah, it may be worth articulating some of the details, design principles that like explain why the Tesla AI chip, or AI computer, essentially, for the car is able to achieve an order of magnitude better processing than anything else that exists. Yeah.

Cool. Thanks. Yeah, I mean, essentially the key is to be able to run the neural net at a bare metal level so that it's especially doing the calculations in the circuits itself and not in some sort of emulation mode which is how a GPU or a CPU would operate. So, you want to do basically a massive amount of localized matrix multiplication with the memory right there. So, it's a huge number of very simple complications with the memory needed to store the results of those complications right next to the circuits that are doing the matrix calculations. And the net effect is an order of magnitude improvement in the frames per second. Our current hardware, which ... I'm a big fan of NVIDIA, they do great stuff but using a GPU, fundamentally it's an emulation mode, and then you also get choked on the bus. So, the transfer between the GPU and the CPU ends up being one that constrains the system. So, the net effect is we're able to, with the Tesla computer ... and we've been like semi-stealth mode basically for the last two to three years on this but I think it's probably time to let the cat out of the bag because the cat's going to come out of the bag anyway but it's an incredible job by Pete and his team to create this, the world's most advanced computer designed specifically for autonomous operation. And there's a rough sort of [Inaudible] whereas the current [Inaudible] hardware can do 200 frames a second, this is able to do over 2,000 frames a second and with full redundancy and fail-over. So, it's an amazing design and we're going to be looking to increase the size of our chip team and our investment in that as quickly as possible. I think we have some of the best aces [Inaudible] in the world but I think we want to build on that even more. And it costs the same as our current hardware and we anticipate that this would have to be replaced, this replacement, which is why I made it easy to switch out the computer, and that's all that needs to be done. If we take out one computer, plug in the next. That's it. All the connectors are compatible and you get an order of magnitude, more processing and you can run all the cameras at primary full resolution with the complex neural net. So it's super kick-ass. Thank you for doing that.

Thanks for making that, and thanks for making the software. Anyway, basically I wanted to introduce three of the key people at Tesla that are doing this. I've huge respect and admiration for you guys and it's because of what you and your team's doing that Tesla will be successful in this arena. Thank you.

Yeah, absolutely. First of all, I'd like to apologize for being impolite on the prior call. Honestly, I think there's really no excuse for bad manners and I was violating my own rule in that regard. Certainly, I have some excuse. There are reasons for it and I'd gotten no sleep and been working sort of 110-hour, 120-hour weeks but, nonetheless, there's still no excuse. My apologies for not being polite on the prior call.

And let's see. With respect to gross margin, I'll touch on that and then hand the rest to Deepak but, certainly, when it's going up the production line, there are a tremendous amount of inefficiencies. There's a lot of hurry up and wait, where some parts of the production line move well. Then, one part doesn't and you have associates waiting around with nothing to do. There are parts that we thought were right but then it turns out they weren't right. We then send them back to the supplier. It's just like the whole sort of giant machine. It just needs to kind of lurch into a high pace and there's a lot of lurching, which is very inefficient. So, you end up having super high labor costs per car and it just takes time to sort of spool up this giant machine. Basically, a production system is like a giant cybernetic collector and it moves as fast as the slowest part. So, as we address those slow parts and as we improve efficiency, gross margin and so the profitability per car just improves dramatically. That's sort of at a high level. Deepak, do you want to add to that?

Actually, a thing that can also happen is that if it turns out, let's say, the production part was either designed wrong or built wrong or there's something wrong with it, then [Inaudible] emergency basis, we have to go with low-volume tooling, which can be produced quickly, but a part produced off of low-volume tooling can easily be 10 times more than a part produced off of production tooling. And so, sometimes what [Inaudible] machine something out of a block and has either that or going to make a car, then the cost of using low-volume cost of use [Inaudible] low volume tooling can be really nutty.

Yeah, I don't know if this trend will continue. We're trying to give you essentially all the information that at least we know of but we're seeing roughly half of all customers choose the Dual Motor or All-Wheel Drive option, which is actually quite a good positive surprise.

Yeah, we don't want to say like this should be assumed to be a continued thing. It's just the thing we are seeing now. Yeah.

It's worth mentioning ... just an interesting little bits of information that Robin was telling me, [Inaudible] doing a great job running worldwide sales [Inaudible] lots of work done, China was really some next level stuff. Robin was born and raised in Shanghai and has been ... along with Tom and Grace and others [Inaudible] team in China has been sort of instrumental in establishing the China factory and making sure that gets done right and having a great relationship with the government. And so it's nice work in that regard. It's really ... I think some of the things people don't expect like what are the top five trading cars for Model 3?

Really surprising.

Right. And we're obviously at this point not yet selling our $35,000 car, so this is promising for the future. All right. Cool. Next question?

Sure. And I would also like to apologize for being impolite on the last call with you. It's not right, and hope you accept my apologies.

So with respect to Gigafactory capex, I think we learned a tremendous amount with Gigafactory 1, and we're confident that we can do the Gigafactory in China for a lot less. I think it's probably closer to ... this is just a guess but probably closer to $2 billion, and that should be at a higher ... and that would be sort of at the 250,000 vehicles per year rate. So I think we can be a lot more efficient with capex, and that would include at least a factory module and pack production, body shop, paint shop and general assembly. Might even be less than that but that's about the right number for that. And then cell production is something we're still figuring out with respect to the Shanghai factory. JB, would you like to add to that?

Yeah, I think, we ... like less than half is like would be a good estimate. And maybe a lot less than half but not more than half would be a fair estimate for capex to get to that 250,000 level. So it's just ... we just learned a tremendous amount about manufacturing, it's like ... it's definitely burned out a lot of neurons, yeah, mental scar tissue, it's [Inaudible] like next level but on the plus side, we really know a lot about volume manufacturing at this point.

Yeah, kind of crazy. Including on the cell ... including the cell production.

Look, what really matters, what actually doesn't matter, things we think matter, and some of it actually ends up not mattering at all.

Yeah. Yes.

Yeah, obviously one of the keys to success on the Model 3 production was the GA4 thing, which was led by Jerome. And General Assembly is key, and doing the sort of Zone 1, 2, semiauto lines, which were critical because we had this fundamental failure especially in Zone 1 ... Zone 2 of factory module production. Thank you, Jerome. It turns out Jerome was pulling some pretty incredible rabbits out of the hat. That was amazing.

And really like what's the point [Inaudible] about the tent but by the way, our tent is amazing and this is not like ... when people like say tent, they'll think it's like some sort of ... something made by REI to go camping. This is a tent that is actually commonly used as a permanent structure. It's a giant thing that is very commonly used as a permanent structure and we just had to come up with a creative solution because GA3 was not going to be able to make the rate and so we had to come up with some ideas, and tell people how that all transpired. It's interesting if you want to...

Yes.

[Inaudible] some of the people [Inaudible]. It's cool. It's great. It is like [Inaudible] really satisfying about building a car.

Especially Model 3. Like it was probably we had two weeks to solve this problem, which is like quasi-impossible. So, we actually didn't have time to order new equipment, because it would have taken too long to arrive. So, we took the conveyors that we discarded from the GA3 line, which didn't work or was way too complex to actually deliver pods. [Inaudible]

Well, I think like the really cool idea was putting them on the 1% grade. So it's like technically the conveyors for parts delivery to GA3 were not graded to be able to move something as heavy as a car, so we made it downhill and on a 1%-downward grade with the car at the top. So then, you can actually overcome the transport...

Yeah, gravity. So, basically, even on your slides, you can do ... accomplish a lot.

Exactly.

And something that's like somewhat counterintuitive is that this actually has fully considered fewer labor hours per car than the GA3 system. And just to elaborate on what Jerome was saying, where we have parts delivery to GA4, the truck literally just backs up to the side of the line, where there is like a door in the tent. And then, that is used to unload parts from suppliers directly to where they are needed on the line. So there's no intermediate assistant. Whereas for GA3, they're unloaded, they're put in a warehouse, then they're repackaged from the warehouse into these totes, which we actually have 220 people, something like that, across all shifts whose only job it was to repackage parts from the boxes that came in from suppliers to the boxes ... to these totes that go into the lifters that go up into GA3. That's literally all they do is move things from one box to another box, and we don't need that at all on GA4.

All gone, yeah. And there's a tremendous amount of 24/7 robotics technicians that are constantly trying to make the machines have uptime. That's very expensive and that's where we figured like not having to maintain all these robotic systems, that's a big cost savings as well. And now we're going to be gradually adding simple automation into GA4 to make it easier to build a car and better sort of labor-saving devices but it's just fundamentally ... it's already at an efficiency level greater than GA3, which is pretty impressive.

We do not ... we will not be raising any equity at any point, at least that's ... I have no expectation of doing so, do not plan to do so. For China, I think, our default plan will be to use essentially a loan from the local banks in China and fund the Gigafactory in Shanghai with local debt, essentially. And we certainly could raise money but I think we don't need to and we ... yeah, I think, it's better to ... it is better discipline not to.

Yeah, our default plan is we pay ... we start paying off our debts. I don't mean refi-ing them, I mean paying them off. For example, there's a convert that's coming due soon, a couple hundred million, $900 million, [Inaudible] something like that. We expect to pay that off with internally generated cash flow.

Yeah.

Yeah, I'm not sure what you're talking about, but there is no such notice from a regulator.

Well, this has never come up. I wouldn't call it weapons grade. It's just like the car is trying to drive and if anything the autonomous cars will be pretty easy to bully because they would optimize so much for avoiding collision. So that will be more of a challenge than anything else is as soon as somebody sees the car's autonomous, they know they can like cut them off and the car is going to do everything it can avoid like a collision. So it's like that will actually be probably a bigger challenge than anything else but we've not encountered anything of the nature of what you're saying.

For Tesla?

I don't think either of them are likely to be. As far as I know, I'm going to be pretty shocked if Amazon has gotten in the car business but I think BMW has great engineering. And it's good to see they're making some investments in electrification. Hopefully, they do more of that. And I'm not sure where they stand on autonomy. It's not on our radar from an autonomy standpoint.

Yeah, we can do a coast-to-coast drive, especially ... like if we pick a specific route and then write code to really make that route work, we could do a coast-to-coast route drive, but that would be kind of gaming the system. And I think it's really important for the autopilot team to be focused on fundamental safety of the existing features. So that's ... the focus is really massively on the safety of existing features. Then there's an advanced dev role that do things like recognize traffic lights and stop signs and make hard right turns and that kind of thing but it's not at the safety level that's considered OK for release. So that ... yeah, because it really, you want many lines of reliability for anything that's released to end customers. So I don't want to take the team off that until we feel like we've really got everything as best we can for the core functionality. Stuart, do you want to add to that?

Yeah, that said, we might be able to pull off coast-to-coast demo before the end of the year if we ... but really like right now if the Subaru [Inaudible] focused on the version 9 software release, which has got a number of really cool things in it. And we're hoping to get that out to early access program in about four weeks and then broadly in September. That's the hardcore focus right now, and that will certainly include some significant advancements in autonomy. And then once that's out and stable, I think that could be a good time to work on the coast-to-coast drive.

Yeah, I think it's extremely powerful once people are comfortable using the technology and see just how much utility it brings. I think that is a very significant potential for margin gain in the future but it's contingent on that functionality really making a difference. I think we will really start to see some of the breakthrough stuff in about a month or so.

[Inaudible].

Like, necessity is the mother of invention, and when you have to do something quickly, then you just don't have time to spend a lot of capital. So it forces you to be capital efficient.

Yeah, I think so, it's still by and large I don't think [Inaudible] we'll be aiming for steel-frame buildings to be clear. It's not like [Inaudible] just become tents everywhere. Yeah.

Yes. Exactly.

Yeah, Model Y is sort of a whole separate thing but it's definitely one of the elements that convinced us that we can scale up quickly and at low capex in Shanghai, where we do an improved version of GA4. And then, we're also figuring out how to make the paint shop a lot simpler and general assembly a lot simpler. And after this call, I'm headed back out to the...

The body shop and making the body shop a lot simpler.

Yeah, we can really simplify the body shop, man. Wow. And there's a lot that we can really easily improve like design to manufacturing and changing some of the joining approaches that we use and actually making the car lighter, cheaper and better and actually stabler. Yeah, it's really, [Inaudible].

Yeah, exactly.

Yes. That's well said. Actually, it's really worth emphasizing JB's point here. Yeah. We're seeing a gain.

Way too fancy.

Start simple and get fancy later. Fancy's going to bite you in the ass.

Yeah, I mean, Gigafactory is ...

Massively automated. It's pretty crazy. And the body production is also heavily automated, almost entirely robots. So it's a mixture of people and automation. There's so much that goes into producing a car going from raw metal and plastic and glass to an actual finished car. And, yeah, as JB was saying, the vast majority of that is highly automated.

The simple answer is yes.

I'm highly confident that it may not be Q1 but I would be shocked if it's not Q2 that we get to 25%.

Well, I don't really know actually how others do it to be totally frank. I just know that the way we ... I see the way we are doing it and I'm told that this is how others do it and we're able to find ways to make it much better. I don't know what the delta would be though.

Yeah. Exactly.

Yeah. In fact, it's amazing how much of production is actually software. We're really quite good at software relative to other car companies and manufacturing at volume is mostly a software problem. I think that was not well appreciated.

And these are cases where we took ... we engaged with companies that were supposed to be world-class experts in automotive production and we just assumed that they would do stuff that worked but it didn't.

Just having that very rapid iteration between design and production is incredibly helpful and we understand for example, what are the rate limiters, what makes it hard to produce battery modules. We came up with a new design that achieves the same outcome, that's actually lighter, better, cheaper and will be introducing that around the end of this year, probably reach volume production on that in Q1 or something. That will make the car lighter, better, and cheaper and achieve a higher range. That line is under construction, will be active in about six months.

Yeah, I mean, because we're sort of desperate to try to get the production working, we actually took a design engineering team and had them work in the factory and improve it, work on production and it's given them tremendous insight into how they need to change the designs in the future to make it easier to produce because you feel the pain directly. Once you feel the pain, like OK, didn't realize I was torturing people with my terrible design. Now I know.

Hello.

Sure.

Sure. He is one of my favorite authors.

And like the logical question is like do we have like a low balance in the bank? The answer is no, we've got ... we're in no ... we're not in any kind of cash shortage at all.

Are we running low on money? The answer is no.

Yeah, I'd say highly confident of being cash-flow positive and being GAAP profitable in Q3.

Is there anything we know at the end of July, it's one month in, we're highly confident of being cash flow positive and GAAP profitable in Q3 and Q4. Now there could be force majeure like an earthquake, touch wood but something like that or massive recession all of a sudden but in the absence of that, of really unusual...

Macro events, yeah.

I think so, yeah. If it's not a million, it's going to be pretty close. I'd say if it's not a million it'd probably be 750,000 or something like that in 2020. So, we're aiming for a million, 2020 but somewhere between half million and a million seems pretty likely.

There's this place called Shanghai.

Not yet.

Maybe. Maybe.

Thank you.

Actually, what we have right now is just the top five. I'm not sure what the allocation is between top five or where it goes beyond the top five. We just sort of out of curiosity asked for the top five breakdowns. And it's just interesting that people are trading up into a Tesla, so they're choosing to spend more money on a Tesla than their current car, just based on the trade-in values. A Civic is a very inexpensive car compared to particularly the Model 3 today. So that's promising from a market-access standpoint but of course, long-term, we're going to do the Model Y and the compact SUV. We're going to do the pickup truck, the Semi, the next generation bus [Inaudible]. We got lots of awesome ideas, and probably the biggest limiter on our growth is like how fast can we grow battery production? And especially cell production and the wholesale supply chain I think will be the fundamental determinant of Tesla's growth.

We're super fired up to do the set. I think they're all super cool. I know Jerome's favorite is the Semi, and that's pretty wicked, obviously. And...

Yeah, it's great. And the [Inaudible] we've made significant improvements to the design since the unveiling that we had, and it's really even better than what we talked about. Probably my personal favorite for the next product is pickup truck, and we are going to just do an amazing pickup truck. And the Model Y, compact SUV, probably the most popular car category in the world, so that's like obviously going to sell pretty well. So a lot of cool things. And of course, Tesla Energy, getting the ... we're kind of cell starved for Powerwall right now, so we actually had to artificially limit the number of Powerwalls because we don't have enough cells. So we're solving for that very rapidly and we expect to ramp up Powerwall and Powerpack production substantially later this year and early next and as well as ramping up retrofit solar and then the Solar Roof. We now have several hundred homes with the Solar Roof on them, and that's going well. It takes a while to just confirm that the Solar Roof is going to last for 30 years and all the details work out, and we're working with first responders to make sure it's safe in the event of a fire and that kind of thing. So it's quite a long validation program for a roof which has got to last for 30, 40, 50 years but we also expect to ramp that up next year at our Gigafactory 2 in Buffalo. That's going to be super exciting. If there's a company with a better product roadmap, I'd like to know where it is, because we've got some super awesome stuff coming. Yeah.

We haven't made a final decision on that.

All right. And actually one of the things I love about your writing is that you really care about getting the details right, and you really understand things well, which is awesome but I have to be careful I don't have a sound bite that is then for those that don't have a nuanced appreciation of the situation, that sounds like then gets ... becomes front-page news. So it's like, nope, that's not what I meant.

Exactly. I'm like, oh, man, this is like shooting myself in the foot there. Right now, the biggest constraint on production again, please, do not make a federal case out of this, because it's something that's solved like in a matter of a week or two, is body production. So that's why ... you can generally tell what am I personally working on, that's going to be a bottleneck in the company most likely, so reducing Model 3 bodies. We've made huge progress in the last few weeks and in fact I was just told that we were able to achieve our first 24 hour period where we made over 800 Model 3 bodies which is pretty great. So [Inaudible] sustain that 800-plus-per-day rate and then [Inaudible] doing great, Jay [Inaudible] is doing great. Yeah, it's good.

Sorry. Go ahead.

All right. Well, thank you for your in-depth coverage of clean-energy technology.

Interesting questions. You always come up with really interesting questions. Really interesting questions that I cannot actually ... the first one I cannot ... it gets so much attention, where we put production. I can't answer any like where we're going to put production questions. Will the Semi use a bunch of Model 3 technology? The answer is yes. Jerome, I'll let you elaborate on that, or it's up to you.

The motors.

These are mad ... at scale, these are insane growth levels.

Yeah, It's not like shipping a software. This is like you actually need to build ... it's like a lot of atoms...

Yes, no, no, I mean like once you build software, you can obviously have lots of copies but like when it's like a lot of really complicated atoms, man, hard.

Oh, yeah.

Yes. We use Samsung and LG and yeah.

It's a partial-sum game. We did shut down a Powerwall cell line in favor of Model 3 to be totally honest but we kind of had to do that but we're adding new cell lines and we'll be able to address that issue very soon.

These are mad growth numbers. Mad.

Yeah, and one of the biggest challenges like, we've got a ... there needs to be a lot more electricians. So we actually had an electrician training program. We're going to actually have to train new people who've never been electricians before to be electricians because otherwise there's not enough electrician capacity in the United States and the most places in the world to install Powerwalls.

So it's like we have to actually literally train electricians and it takes like two years basically before somebody is certified to be an electrician. So it's sort of like, OK, we obviously can't grow faster than the rates, the number of electricians who can physically install a Powerwall. That's like one of the limitations.

Yeah, it's awesome actually.

[Inaudible] say anything that's like [Inaudible].

Yeah, gigawatt hour. That's public, right?

OK.

OK. All right, OK.

And there were like so many people who had said 1 gigawatt hour is an impossible number for lithium ion. Like that's ... yeah.

Yeah, if you extrapolate energy growth rate, well, obviously, if you extrapolate anything, when that triples for a year pretty soon becomes the size of the universe but long-term we would expect the energy business to catch up to the auto business in size.

Good question. We try to anticipate ... actually, we try and anticipate the questions that are on people's minds, that's why we have the autopilot [Inaudible] autopilot team here and much of the executive team of Tesla here to try to be proactive in that regard. And is there anything...

I think we really covered a lot. So if there's any ... yeah.

Your very last thing. Go ahead.

Yeah, being cash flow positive and capping at positive doesn't mean like ... doesn't mean we're rolling in money. There's definitely going to be cases where we're just barely cash flow positive or barely profitable in some quarters in the future but I think it's been a long time, almost 15 years now. I think we're at a scale where the amount of time that it takes to actually scale up and do things is ... there's a certain ... like we're big enough, where we actually can spend money efficiently to make things go faster. So we kind of hit scale with volume production of cars. And I think we can ... I think this is probably the right thing to do is to be sort of essentially self-funding on a go forward basis and apart from selective situations where there's say some debt ... temporary debt for construction of a Gigafactory in China or Europe or something like that but apart from that, I think we ... essentially like I don't think we're constraining growth in any significant way by adopting this strategy at this point. It would have been true in times past but I think it is no longer the case, yeah.
