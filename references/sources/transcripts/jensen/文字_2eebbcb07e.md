# NVIDIA Q1 FY2024 earnings call

- 人物: jensen
- 视频编号: 文字_2eebbcb07e
- 频道: 文字稿
- 日期: 2023-05-24
- 分类: earnings_call
- 链接: https://www.fool.com/earnings/call-transcripts/2023/05/24/nvidia-nvda-q1-2024-earnings-call-transcript/
- 来源: 网站整理的文字稿(Professional transcript, Huang's lines only),只含本人发言,原稿无时间戳

---

I thought that was great, Colette. Thank you.

Yes, C.J. Thanks for the question. I'll start backwards. The -- remember, we were in full production of both Ampere and Hopper when the ChatGPT moment came.

And it helped everybody crystallize how to transition from the technology of large language models to a product and service based on a chatbot. The integration of guardrails and alignment systems with reinforcement learning from human feedback, knowledge vector databases for proprietary knowledge, connection to search, all of that came together in a really wonderful way. And it's -- the reason why I call it the iPhone moment, all the technology came together and helped everybody realize what an amazing product it can be and what capabilities it can have. And so, we were already in full production.

NVIDIA's supply chain flow and our supply chain is very significant, as you know. And we build supercomputers in volume, and these are giant systems, and we build them in volume. It includes, of course, the GPUs. But on our GPUs, the system boards have 35,000 other components.

And the networking and the fiber optics and the incredible transceivers and the NICs, the SmartNICs, the switches, all of that has to come together in order for us to stand up a data center. And so, we were already in full production when that moment came. We had to really significantly increase our procurement substantially for the second half, as Colette said. Now, let me talk about the bigger picture and why the entire world's data centers are moving toward accelerated computing.

It's been known for some time, and you've heard me talk about it, that accelerated computing is a full stack problem but -- is full stack challenged. But if you could successfully do it in a large number of application domain that's taken us 15 years, it's sufficiently that almost the entire data centers' major applications could be accelerated, you could reduce the amount of energy consumed and the amount of cost for our data center substantially by an order of magnitude. It costs a lot of money to do it because you have to do all the software and everything, and you have to build all the systems and so on and so forth. But we've been at it for 15 years.

And what happened is when generative AI I came along, it triggered a killer app for this computing platform that's been in preparation for some time. And so, now, we see ourselves in two simultaneous transitions: the world's $1 trillion data center is nearly populated entirely by CPUs today. And $1 trillion is $250 billion a year. It's growing, of course.

But over the last four years, call it $1 trillion worth of infrastructure installed, and it's all completely based on CPUs and dumb NICs. It's basically unaccelerated. In the future, it's fairly clear now with this -- with generative AI becoming the primary workload of most of the world's data centers generating information, it is very clear now that -- and the fact that accelerated computing is so energy-efficient, that the budget of a data center will shift very dramatically toward accelerated computing, and you're seeing that now. We're going through that moment right now as we speak while the world's data center capex budget is limited.

But at the same time, we're seeing incredible orders to retool the world's data centers. And so, I think you're starting -- you're seeing the beginning of, call it, a 10-year transition to basically recycle or reclaim the world's data centers and build it out as accelerated computing. You'll have a pretty dramatic shift in the spend of a data center from traditional computing and to accelerate computing with SmartNICs, smart switches, of course, GPUs and the workload is going to be predominantly generative AI.

Regarding competition, we have competition from every direction, start-ups, really, really well funded and innovative start-ups, countless of them all over the world. We have competitions from existing semiconductor companies. We have competition from CSPs with internal projects, and many of you know about most of these. And so, we're mindful of competition all the time, and we get competition all the time.

NVIDIA's value proposition at the core is we are the lowest cost solution. We're the lowest TCO solution. And the reason for that is because accelerated computing is two things that I talked about often, which is it's a full stack problem. It's a full stack challenge.

You have to engineer all of the software and all the libraries and all the algorithms, integrate them into and optimize the frameworks and optimize it for the architecture of not just one chip but the architecture of an entire data center all the way into the frameworks, all the way into the models. And the amount of engineering and distributed computing -- fundamental computer science work is really quite extraordinary. It is the hardest computing as we know. And so, number one, it's a full stack challenge, and you have to optimize it across the whole thing and across just a mind-blowing number of stacks.

We have 400 acceleration libraries. As you know, the amount of libraries and frameworks that we accelerate is pretty mind-blowing. The second part is that generative AI is a large-scale problem and it's a data center scale problem. It's another way of thinking that the computer is the data center or the data center is the computer.

It's not the chip, it's the data center. And it's never happened like this before. And in this particular environment, your networking operating system, your distributed computing engines, your understanding of the architecture of the networking gear, the switches, and the computing systems, the computing fabric, that entire system is your computer. And that's what you're trying to operate.

And so, in order to get the best performance, you have to understand full stack and understand data center scale. And that's what accelerated computing is. The second thing is that utilization, which talks about the amount of the types of applications that you can accelerate and the versatility of your architecture keeps that utilization high. If you can do one thing and do one thing only incredibly fast, then your data center is largely underutilized, and it's hard to scale that out.

NVIDIA's universal GPU, the fact that we accelerate so many of these stacks, makes our utilization incredibly high. And so, number one is steer put, and that's software-intensive problems and data center architecture problem. The second is digitalization versatility problem. And the third, it's just data center expertise.

We've built five data centers of our own, and we've helped companies all over the world build data centers. And we integrate our architecture into all the world's clouds. From the moment of delivery of the product to the standing up and the deployment, the time to operations of a data center is measured not -- it can -- if you're not good at it and not proficient at it, it could take months. Standing up a supercomputer -- let's see.

Some of the largest supercomputers in the world were installed about 1.5 years ago, and now they're coming online. And so, it's not unheard of to see a delivery to operations of about a year. Our delivery to operations is measured in weeks. And that's -- we've taken data centers and supercomputers, and we've turned it into products.

And the expertise of the team in doing that is incredible. And so, our value proposition is in the final analysis. All of this technology translates into infrastructure, the highest throughput and the lowest possible cost. And so, I think our market is, of course, very, very competitive, very large, but the challenge is really, really great.

Yes. We can see in real time the growth of generative AI in CSPs, both for training the models, refining the models, as well as deploying the models. As Colette said earlier, inference is now a major driver of accelerated computing because generative AI is used so capably in so many applications already. There are two segments that require a new stack of software, and the two segments are enterprise and industrials.

Enterprise requires a new stack of software because many enterprises need to have all the capabilities that we've talked about, whether it's large language models, the ability to adapt them for your proprietary use case, and your proprietary data and alignment to your own principles and your own operating domains. You want to have the ability to be able to do that in a high-performance computing sandbox, and we call that DGX Cloud and -- to create that model. Then, you want to deploy your chatbot or your AI in any cloud because you have services and you have agreements with multiple cloud vendors and depending on the applications, you might deploy it on various clouds. And for the enterprise, we have NVIDIA AI Foundations for helping you create custom models, and we have NVIDIA AI Enterprise.

NVIDIA AI Enterprise is the only accelerated stack -- GPU accelerated stack in the world that is enterprise safe and enterprise supported. There are constant patching that you have to do. There are 4,000 different packages that build up NVIDIA AI Enterprise and represents the operating engine -- end-to-end operating engine of the entire AI workflow. It's the only one of its kind from data ingestion, data processing.

Obviously, in order to train an AI model, you have a lot of data you have to process and package up and curate and align. And there's just a whole bunch of stuff that you have to do to the data to prepare it for training. That amount of data could consume some 40%, 50%, 60% of your computing time. And so, data processing is a very big deal.

And then, the second aspect of it is training the model, refining the model. And the third is deploying model for inferencing.NVIDIA AI Enterprise supports and patches and security patches continuously all of those 4,000 packages of software. And for an enterprise that wants to deploy their engines just like they want to deploy Red Hat Linux, this is incredibly complicated software. In order to deploy that in every cloud and as well as on-prem, it has to be secure.

It has to be supported. And so, NVIDIA AI Enterprise is the second part. The third is Omniverse. Just as people are starting to realize that you need to align an AI to ethics, the same for robotics.

You need to align the AI for physics, and aligning an AI for ethics includes a technology called reinforcement learning human feedback. In the case of industrial applications and robotics, it's reinforcement learning Omniverse feedback. And Omniverse is a vital engine for software-defined and robotic applications and industries. And so, Omniverse also needs to be a cloud service platform.

And so, our software stack, the three software stacks, AI Foundations, AI Enterprise, and Omniverse, runs in all of the world's clouds that we have partnerships, DGX Cloud partnerships with. Azure, we have partnerships on both AI, as well as Omniverse. With GCP and Oracle, we have great partnerships in DGX Cloud for AI, and AI Enterprise is integrated into all three of them. And so, I think the -- in order for us to extend the reach of AI beyond the cloud and into the world's enterprise and into the world's industries, you need two new types of -- you need new software stacks in order to make that happen.

And by putting it in the cloud, integrated into the world CSP clouds, it's a great way for us to partner with the sales and the marketing team and the leadership team of all the cloud vendors.

Colette, how about you go first? You take the question first.

InfiniBand and ethernet are -- target different applications in a data center. They both have their place. InfiniBand had a record quarter. We're going to have a giant record year.

And InfiniBand has a really -- NVIDIA's Quantum InfiniBand has an exceptional road map. It's going to be really incredible. The two networks are very different. InfiniBand is designed for an AI factory, if you will.

If that data center is running a few applications for a few people for a specific use case and is doing it continuously, and that infrastructure costs you, pick a number, $500 million. The difference between InfiniBand and ethernet could be 15%, 20% in overall throughput. And if you spent $500 million on an infrastructure and the difference is 10% to 20%, and it's $100 million, InfiniBand's basically free. That's the reason why people use it.

InfiniBand is effectively free. The difference in data center throughput is just -- it's too great to ignore. And you're using it for that one application. And so -- however, if your data center is a cloud data center and it's multi-tenant, it's a bunch of little jobs, a bunch of little jobs and is shared by millions of people, then ethernet is really the right answer.

There's a new segment in the middle where the cloud is becoming a generative AI cloud. It's not an AI factory per se, but it's still a multi-tenant cloud, but it wants to run generative AI workloads. This new segment is a wonderful opportunity. And at COMPUTEX -- I referred to it at the last GTC.

At COMPUTEX, we're going to announce a major product line for this segment, which is for ethernet-focused generative AI application type of clouds. But InfiniBand is doing fantastically, and we're doing record numbers quarter on quarter, year on year.

Yeah. I'll work backwards. You're never done with training. You're always -- every time you deploy, you're collecting new data.

When you collect new data, you train with the new data. And so, you're never done training. You're never done producing and processing a vector database that augments the large language model. You're never done with vectorizing all of the collected structured, unstructured data that you have.

And so, whether you're building a recommender system, a large language model, a vector database, these are probably the three major applications of -- the three core engines, if you will, of the future of computing, as well as a bunch of other stuff. But obviously, these are very -- three very important ones. They are always, always running. You're going to see that more and more companies realize they have a factory for intelligence -- an intelligence factory.

And in that particular case, it's largely dedicated to training and processing data and vectorizing data and learning representation of the data, so on and so forth. The inference part of it are APIs that are either open APIs that can be connected to all kinds of applications, APIs that are integrated into workflows but APIs of all kinds. There will be hundreds of APIs in a company. Some of them, they built themselves.

Some of them, part that -- many of them could come from companies like ServiceNow and Adobe that we're partnering with in AI Foundations. And they'll create a whole bunch of generative AI APIs that companies can then connect into their workflows or use as an application. And, of course, there'll be a whole bunch of internet service companies. And so, I think you're seeing for the very first time, simultaneously, a very significant growth in the segment of AI factories, as well as a market that -- a segment that really didn't exist before but now it's growing exponentially, practically by the week, for AI inference with APIs.

The simple way to think about it in the end is that the world has a $1 trillion of data center installed, and it used to be 100% CPUs. In the future, we know -- we've heard it in enough places, and I think this year's ISC keynote was actually about the end of Moore's Law. We've seen it in a lot of places now that you can't reasonably scale out data centers with general purpose computing and that accelerated computing is the path forward. And now, it's got a killer app.

It's called generative AI. And so, the easiest way to think about that is your $1 trillion infrastructure. Every quarter's capital, capex budget would lean very heavily into generative AI, into accelerated computing infrastructure, everywhere from the number of GPUs that would be used in the capex budget to the accelerated switches and accelerated networking chips that connect them all. The easiest way to think about that is, over the next four, five, 10 years, most of that $1 trillion and then compensating, adjusting for all the growth in data center still, it will be largely generative AI.

And so, that's probably the easiest way to think about that, and that's training as well as inference.

Yeah. That's a great question. Whether you're -- whether -- you start by building a large language model, and you use that large language model, very large version, and you could distill them into medium, small, and tiny size. And the tiny sized ones, you could put in your phone and your PC and so on and so forth.

And they all have good -- they all have -- it seems surprising, but they all can do the same thing. But obviously, the zero shot or the generalizability of the large language model, the biggest one is much more versatile, and it can do a lot more amazing things. And the large one would teach the smaller ones how to be good AIs, and so you use the large one to generate prompts to align the smaller ones and so on and so forth. And so, you start by building very large ones, and then you also have to train a whole bunch of smaller ones.

That's exactly the reason why we have so many different sizes of our inference. You saw that I announced L4, L40, H100 NVL, which also has H100. And then, it has -- and then, we have H100 HGX, and then we have H100 multinode with NVLink. And so, there's a -- you could have model sizes of any kind that you like.

The other thing that's important is these are models, but they're connected ultimately to applications. And the applications could have image in, video out, video in, text out, image in, proteins out, text in, 3D out, video in, in the future, 3D graphics out. So, the input and the output requires a lot of pre and postprocessing. The pre and postprocessing can't be ignored.

And this is one of the things that most of the specialized chip arguments fall apart. And it's because the length -- the model itself is only, call it, 25% of the data -- of the overall processing of inference. The rest of it is about preprocessing, postprocessing, security, decoding, all kinds of things like that. And so, I think the -- we -- the multi-modality aspect of inference, the multidiversity of inference that it's going to be done in the cloud on-prem, it's going to be done in multi-cloud.

That's the reason why we have AI Enterprise in all the clouds. It's going to be done on-prem. It's the reason why we have a great partnership with Dell we just announced the other day called Project Helix. That's going to be integrated into third-party services.

That's the reason why we have a great partnership with ServiceNow and Adobe because they're going to be creating a whole bunch of generative AI capabilities. And so, there's a -- the diversity and the reach of generative AI is so broad, you need to have some very fundamental capabilities like what I just described in order to really address the whole space of it.

Yeah. Harlan, I really appreciate that. Nearly everybody who thinks about AI, they think about that chip, that accelerator chip. And in fact, this is the whole point nearly completely.

And I've mentioned before that accelerated computing is about the stack, about the software. And networking, remember, we announced very, very early on this networking stack called DOCA, and we have an acceleration library called Magnum IO. These two pieces of software are some of the crown jewels of our company. Nobody ever talks about it because it's hard to understand, but it makes it possible for us to connect tens of thousands of GPUs.

How do you connect tens of thousands of GPUs if the operating system of the data center, which is the infrastructure, is not insanely great? And so, that's the reason why we're so obsessed about networking in the company. And one of the great things that we have, we have Mellanox, as you know quite well, was the world's highest performance and the unambiguous leader in high-performance networking. It's the reason why our two companies are together. You also see that our network expands starting from NVLink, which is a computing fabric with really super low latency, and it communicates using memory references, not network packaged.

And then, we take NVLink. We connect it inside multiple GPUs, and I've described going beyond the GPU. And I'll talk a lot more about that at COMPUTEX in a few days. And then that gets connected to InfiniBand, which includes the NIC and the SmartNIC, BlueField-3 that we're in full production with and the switches.

All of the fiber optics that are optimized end to end, these things are running at incredible line rates. And then, beyond that, if you want to connect the smart AI factory -- this AI factory into your computing fabric, we have a brand-new type of ethernet that we'll be announcing at COMPUTEX. And so the -- this whole area of the computing fabric extending -- connecting all of these GPUs and computing units together all the way through the networking, through the switches, the software stack is insanely complicated. And so, we're -- I'm delighted you understand it, and -- but we don't break it out particularly because we think of the whole thing as a computing platform as it should be.

We sell it to all of the world's data centers as components so that they can integrate it into whatever style or architecture that they would like and we can still run our software stack. That's the reason why we break it up. It's way more complicated the way that we do it, but it makes it possible for NVIDIA's computing architecture to be integrated into anybody's data center in the world from cloud of all different kinds to on-prem of all different kinds, all the way out to the edge to 5G. And so, this way of doing it is really, really complicated, but it gives us incredible reach.

Yeah. Thanks, Matt. It's -- without being too specific about numbers, but the ideal scenario, the ideal mix is something like 10% NVIDIA DGX Cloud and 90% the CSPs' clouds. And the reason -- and our DGX Cloud is the NVIDIA stack.

It's the pure NVIDIA stack. It is architected the way we like and achieves the best possible performance. It gives us the ability to partner very deeply with the CSPs to create the highest-performing infrastructure, number one. Number two, it allows us to partner with the CSPs to create markets.

Like for example, we're partnering with Azure to bring Omniverse Cloud to the world's industries. And the world has never had a system like that, the computing stack with all the generative AI stuff and all the 3D stuff and the physics stuff, incredibly large database and really high-speed networks and low-latency networks. That kind of a virtual -- industrial virtual world has never existed before. And so, we partnered with Microsoft to create Omniverse Cloud inside Azure Cloud.

And so, it allows us, number two, to create new applications together and develop new markets together. And we go to market as one team. And we benefit by getting customers on our computing platform, and they benefit by having us in their cloud, number one. But number two, the amount of data and services and security services and all of the amazing things that Azure and GCP and OCI have, they can instantly have access to that through Omniverse Cloud.

And so, it's a huge win-win. And for the customers, the way that NVIDIA's cloud works for these early applications, they could do it anywhere. So, one standard stack runs in all the clouds. And if they would like to take their software and run it on the CSP's cloud themselves and manage it themselves, we're delighted by that because NVIDIA AI Enterprise, NVIDIA AI Foundations, and long term, this is going to take a little longer, but NVIDIA Omniverse will run in the CSP's clouds.

OK? So, our goal really is to drive architecture, to partner deeply in creating new markets and the new applications that we're doing and provide our customers with the flexibilities to run NVIDIA everywhere, including on-prem. And so, that -- those were the primary reasons for it. And it's worked out incredibly. Our partnership with the three CSPs and that we currently have DGX Cloud in and their sales force and marketing teams, their leadership teams is really quite spectacular.

The computer industry is going through two simultaneous transitions, accelerated computing and generative AI. CPU scaling has slowed, yet computing demand is strong, and now, with generative AI, supercharged. Accelerated computing, a full stack and data center scale approach that NVIDIA pioneered is the best path forward. There's $1 trillion installed in the global data center infrastructure based on the general purpose computing method of the last era.

Companies are now racing to deploy accelerated computing for the generative AI era. Over the next decade, most of the world's data centers will be accelerated. We are significantly increasing our supply to meet their surging demand. Large language models can learn information encoded in many forms.

Guided by large language models, generative AI models can generate amazing content with models to fine-tune, guardrail, align to guiding principles. And ground -- ground to facts, generative AI is emerging from labs and is on its way to industrial applications. As we scale with cloud and internet service providers, we are also building platforms for the world's largest enterprises. Whether within one of our CSP partners or on-prem with Dell Helix, whether on a leading enterprise platform like ServiceNow and Adobe or bespoke with NVIDIA AI Foundations, we can help enterprises leverage their domain expertise and data to harness generative AI securely and safely.

We are ramping a wave of products in the coming quarters, including H100, our Grace and Grace Hopper Superchips and our BlueField-3 and Spectrum-4 networking platform. They are all in production. They will help deliver data center scale computing that is also energy-efficient and sustainable computing. Join us next week at COMPUTEX, and we'll show you what's next.
