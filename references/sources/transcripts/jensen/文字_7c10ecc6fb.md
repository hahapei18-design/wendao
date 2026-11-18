# NVIDIA Q3 FY2024 earnings call

- 人物: jensen
- 视频编号: 文字_7c10ecc6fb
- 频道: 文字稿
- 日期: 2023-11-22
- 分类: earnings_call
- 链接: https://www.fool.com/earnings/call-transcripts/2023/11/22/nvidia-nvda-q3-2024-earnings-call-transcript/
- 来源: 网站整理的文字稿(Professional transcript, Huang's lines only),只含本人发言,原稿无时间戳

---

Generative AI is the largest TAM expansion of software and hardware that we've seen in several decades. At the core of it, what's really exciting is that what was largely a retrieval-based computing approach, almost everything that you do as we treated off of storage somewhere. As has been augmented now add it with a generative method, and it's changed almost everything. You could see that text to text, text to image, text to video, text to 3D, text to protein, text to chemicals.

These are things that were processed and typed by humans in the past, and these are now generative approaches. The way that we access data has changed. It used to be based on explicit queries, it is now based on natural language queries, intention queries, semantic queries. And so, we're excited about the work that we're doing with SAP and Dropbox and many others that you're going to hear about.

And one of the areas that is really impactful is the software industry, which is about $1 trillion or so has been building tools that are manually used over the last couple of decades. And now, there's a whole new segment of software called copilots and assistants, instead of manually use these tools will have copilots to help you use it. And so, instead of licensing software, we will continue to do that, of course, but we will also hire copilots and assistants to help us use the -- use the software. We'll connect all of these copilots and systems into teams of AI, which is going to be the modern version of software, modern version of enterprise business software.

And so, the transformation of software and the way that software is done is driving the hardware underneath. And you can see that it's transforming in two ways. One is something that's largely independent of generative AI. There's two trends.

One is related to accelerated computing. General-purpose computing is too wasteful of energy and cost. And now that we have a much, much better approaches called accelerated computing, you could save an order of magnitude of energy, you could save an order of magnitude of time where you can save an order of magnitude of cost by using acceleration. And so, accelerated computing is transitioning, if you will, general-purpose computing into this new approach.

And that has been augmented by a new class of data centers. This is the traditional data centers that you were just talking about, where we represent about a third of that. But there's a new class of data centers. And this new class of data centers, unlike the data centers of the past where you have a lot of applications running used by a great many people that are different tenants that are using the same infrastructure, and the data center stores a lot of files.

These new data essentials are very few applications if not one application used by basically one tenant. And it processes data. It trains models and it generates tokens, it generates AI. And we call these new data center AI factories.

We're seeing AI factories being built out everywhere in just about every country. And so, if you look at the way where we are in the expansion, the transition into this new computing approach, the first wave you saw with large language model start-ups, generative AI start-ups, and consumer Internet companies. And we're in the process of ramping that. Meanwhile, that's being ramped.

You see that we're starting to partner with enterprise software companies who would like to build chatbots and copilots and assistants to augment the tools that they have on their platforms. You're seeing GPU-specialized CSPs cropping up all over the world, and they're dedicated to doing really one thing, which is processing AI. You're seeing sovereign AI infrastructures, people, countries that now recognize that they have to utilize their own data, keep their own data, keep their own culture, process that data, and develop their own AI. You see that in India.

Several -- about a year ago in Sweden, you're seeing in Japan. Last week, a big announcement in France. But the number of sovereign AI clouds that are being built is really quite significant. And my guess is that almost every major region will have, and surely, every major country will have their own AI cloud.

And so, I think you're seeing just new developments as the generative AI wave propagates through every industry, every company, every region. And so, we're at the beginning of this inflection, this computing transition.

Yeah. Thanks for the question. Our networking business is already at a $10 billion-plus run rate. And it's going to get much larger.

And as you mentioned, we added a new networking platform to our networking business recently. The vast majority of the dedicated large-scale AI factories standardized on InfiniBand. And the reason for that is really because of its data rate and not only just the latency but the way that it moves traffic around the network is really important. The way that you process AI and a multi-tenant hyperscale Ethernet environment, the traffic pattern is just radically different.

And with InfiniBand and with software-defined networks, we could do congestion control, adaptive routing, performance isolation, and noise isolation, not to mention, of course, the data rate and the low latency that -- and the very low overhead of InfiniBand that's a natural part of InfiniBand. And so, InfiniBand is not so much just a network. It's also a computing fabric. We put a lot of software-defined capabilities into the fabric, including computation.

We do floating point calculations and computation right on the switch and right in the fabric itself. And so, that's the reason why that difference in Ethernet versus InfiniBand where InfiniBand versus Ethernet for AI factories is so dramatic. And the difference is profound and the reason for that is because you've just invested in a $2 billion infrastructure for AI factories, a 20%, 25%, 30% difference in overall effectiveness, especially as you scale up is measured in hundreds of millions of dollars of value. And if you were renting that infrastructure over the course of four or five years, it really adds up.

And so, InfiniBand's value proposition is undeniable for AI factories. However, as we move AI into enterprise, this is enterprise computing where we'd like to enable every company to be able to build their own custom AI. We're building customer AIs in our company based on our proprietary data, our proprietary type of skills. For example, recently, we spoke about one of the models that we're creating.

It's called Chip Nemo. We're building many others. There'll be tens, hundreds of custom AI models that we create inside our company. And our company is -- for all of our employees, doesn't have to be as high performance as the AI factories, we use to train the models.

And so, we would like the AI to be able to run an Ethernet environment. And so, what we've done is we invented this new platform that extends Ethernet. It doesn't replace the Ethernet, it's 100% compliant with Ethernet, and it's optimized for east-west traffic, which is where the computing fabric is. It adds to Ethernet with an end-to-end solution with Bluefield as well as our Spectrum switch that allows us to perform some of the capabilities that we have in InfiniBand, not all but some, and we achieved excellent results.

And the way we go to market is we go to market with our large enterprise partners who already offer our computing solution. And so, HPL and Lenovo have the NVIDIA AI stack, the NVIDIA enterprise software stack. And now they integrate with BlueField as well as bundle take to market their Spectrum switch and they'll be able to offer enterprise customers all over the world with their vast sales force and vast network of resellers the -- in a fully integrated, if you will, fully optimized at least end-to-end AI solution. And so, that's basically bringing AI to Ethernet for the world's enterprise.

Yeah. Thanks for your question. Grace Hopper is in production in high-volume production now. We're expecting next year just with all of the design wins that we have in high-performance computing and AI, AI infrastructures.

We are on a very, very fast ramp with our first data center CPU to a multibillion-dollar product line. This is going to be a very large product line for us. The capability of Grace Hopper is really quite spectacular. It has the ability to create compute nodes that simultaneously have very fast memory as well as very large memory.

In the areas of vector databases or semantic search, what is called REG, retrieval augmented generation, so that you could have a generative AI model, be able to refer to proprietary data or factful data before it generates a response. That data is quite large. And you could also have applications or generative models where the context length is very high. You basically store an entire book into its system memory before you ask a question.

And so, the context link can be quite large. This way, the degenerative models have the ability to still be able to naturally interact with you on one hand, on the other hand, be able to refer to factual data, proprietary data or domain-specific data, newer data, and be continually relevant and reduce hallucination. And so, that particular use case, for example, is really quite fantastic for Grace Hopper. It also serves the customers that really care to have a different CPU the X86, maybe it's European supercomputing centers or European companies who would like to build up their own ARM ecosystem and I'd like to build up a stack or CSPs that have decided that they would like to pivot ARM because their own custom CPUs are based on ARM.

There are a variety of different reasons that drives the success of Grace Hopper, but we're off to just an extraordinary start. This is a home run product.

Absolutely believe that data center can grow through 2025. And there are, of course, several reasons for that. We are expanding our supply quite significantly. We have already won the broadest and largest and most capable supply chain in the world.

Remember, people think that the GPU is a chip, but the HGX, H100, the Hopper HGX has 35,000 parts. It weighs 70 pounds. Eight of the chips are Hopper. The other 35,000 are not.

It is -- it has -- even its passive components are incredible, high-voltage parts, high-frequency parts, high-current parts. It is a supercomputer and therefore, the only way to test the supercomputers with another supercomputer. Even the manufacturing of it is complicated, the testing of it is complicated, the shipping event is complicated, and installation is complicated. And so, every aspect of our HGX supply chain is complicated.

And the remarkable team that we have here has really scaled out the supply chain incredibly not to mention all of our HDX are connected with MBA networking and the networking, the transceivers, the mics, the cables, the switches, the amount of complexity there is just incredible. And so, I'm just -- first of all, I'm just super proud of the team for scaling up this incredible supply chain. We are absolutely world-class. But meanwhile, we're adding new customers and new products.

So, we have new supply. We have new customers. As I was mentioning earlier, different regions are standing up GPU specialist clouds. Sovereign AI clouds coming up from all over the world as people realize that they can't afford to export their country's knowledge, their country's culture for somebody else to then resell AI back to them.

They have to -- they should. They have the skills and fairly with us, in combination, we can help them do that, build up their national AI. And so, the first thing that they have to do is create their AI cloud national AI cloud. You're also seeing us now growing into enterprise.

The enterprise market has two paths, one path, or if I could say, three paths. The first half, of course, off-the-shelf AI. And there are, of course, Chat-GPT fabulous off-the-shelf AI, there'll be others. There's also a proprietary AI because the software companies like ServiceNow and SAP and there are many, many others, I can't afford to have their company's intelligence be outsourced to somebody else.

And they are about building tools. And on top of their tools, they should build custom and proprietary, and domain-specific copilots and assistants that they can rent to their customer base. This is -- they're sitting on a gold mine. Almost every major tools company in the world is sitting on gold mine, and they recognize that.

They have to go build their own custom AIs. We have a new service called an AI Foundry, where we leverage NVS capabilities to be able to serve them in that. And then the next one is on enterprises building their own custom AI their own custom chatbots, their own custom. And this capability is spreading all over the world.

And the way that we're going to serve that marketplace is with the entire stacks of systems, which includes our compute, our networking and our switches running our software stack called NVIDIA AI enterprise taking it through our market partners, HP, Dell, and Lenovo, so on and so forth. And so, we're just -- we're seeing the waves of generative AI starting from the start-ups and CSPs moving to consumer Internet companies moving to enterprise software platforms, moving to enterprise companies. And then -- and ultimately, one of the areas that you guys have seen us spend a lot of energy on has to do with industrial generative AI. This is where NVIDIA AI and NVIDIA Omniverse comes together.

And that is a really, really exciting work. And so, I think the -- we're at the beginning of a and basically across-the-board industrial transition to generative AI to accelerated computing. This is going to affect every company, every industry, every country.

Thanks for the question. There is a glaring opportunity in the world for AI foundry. And it makes so much sense. First, every company has its core intelligence.

It makes up our company. Our data, our domain expertise. In the case of many companies, we create tools. And most of the software companies in the world are tool platforms.

And those tools are used by people today. And in the future, it's going to be used by people augmented with a whole bunch of AIs that we hire. And these platforms just got to go across the world, and you'll see, and we've already announced a few SAP, ServiceNow, Dropbox, Getty, many others are coming. And the reason for that is because they have their own proprietary AI, and they want their own proprietary AI.

They can't afford to outsource their intelligence and hand out their data and hand out their flywheel for other companies to build the AI for them. And so, they come to us. We have several things that are really essential in the foundry, just as TSMC is a foundry, you have to have AI technology. And as you know, we have just an incredible depth of capability, AI technology capability.

And then second, you have to have the best practice known practice, the skills of processing data through the invention of AI models to create AIs that are guardrails fine-tuned, so on and so forth that are safe, so on and so forth. And the third thing is unique factories, and that's what DGX Cloud is. Our AI models are called AI foundations. Our process, if you will, our CAD systems for creating AIs are called NEMO, and they run on NVIDIA factories we call DGX Cloud.

Our monetization model is that with each one of our partners, they rent a sandbox on DGX Cloud where we work together. They bring their data. They bring their domain expertise. We've got our researchers and engineers.

We help them build their custom AI. We help them make that custom AI incredible. Then that customer AI becomes theirs, and they deploy it on a run time that is enterprise-grade, enterprise-optimized, or outperformance-optimized runs across everything NVIDIA. We have a giant installed base in the cloud on-prem anywhere.

And it's secure, securely patched, constantly patched and optimized and supported. And we call that NVIDIA AI enterprise. NVIDIA AI Enterprise is $4,500 per GP per year. That's our business model.

Our business model is basically a license. Our customers then, with that basic license, can build their monetization model on top of. In a lot of ways, we're wholesale. They become retail.

They could have a per-subscription license base. They could per instance, or they could do per usage. There's a lot of different ways that they could take to create their own business model, but ours is basically like a software license like an operating system. And so, our business model is help you create your custom models, you run those custom models on NVIDIA AI Enterprise.

And it's off to a great start. NVIDIA AI Enterprise is going to be a very large business for us.

Sure. Inference, inference is complicated. It's actually incredibly complicated. If you – we, this quarter, announced one of the most exciting new engines optimizing compilers called TensorRT LM.

The reception has been incredible. You go to GitHub. It's been downloaded a ton, a whole lot of stars integrated into stacks and frameworks all over the world, almost instantaneously. And there are several reasons for that, obviously.

We could create TensorRT LLM because CUDA's programmable. If CUDA and our GPUs were not so programmable, it would really be hard for us to improve software stacks at the pace that we do. TensorRT LLM on the same GPU without anybody touching anything, improves the performance by a factor of two. And then on top of that, of course, the pace of our innovation is so high.

H200 increases it by another factor of two. And so, our inference performance another way of saying inference cost just reduced by a factor of four within about a year's time. And so, that's really, really hard to keep up with. Now, the reason why everybody likes our inference engine is because our installed base.

And we've been dedicated to our installed base for 20 years, 20-plus years. We have an installed base that is not only largest in every single cloud, it's in every available from every enterprise system maker. It's used by companies of just about every industry. And any time you see an NVIDIA GPU, it runs our stack.

It's architecturally compatible. It's something we've been dedicated to for a very long time. We're very disciplined about it. We make it, if you will, architecture compatibility is job one.

And that has conveyed to the world the certainty of our platform stability. NVIDIA's platform stability certainty is the reason why everybody builds on us first and the reason why everybody optimizes on us first. All the engineering and all the work that you do, all the invention of technologies that you build on top of NVIDIA accrues to the -- and benefits everybody that uses our GPUs, and we have such a large installed base, millions and millions of GPUs in cloud, 100 million GPU from people's PCs, just about every workstation in the world, and they're all architecturally compatible. And so, if you're an inference platform and you are deploying an inference application, you are basically an application provider and as a software application provider, and you're looking for a large installed base.

Data processing, before you could train a model, you have to augment the data. You have to debug the data, maybe you have to augment the data with synthetic data. So, you process that they clean the data, align the data, normalize the data, all of that data is measured not in bites and megabytes. It's measured in terabytes and petabytes.

And the amount of data processing that you do before data engineering before that you do training is quite significant. It could represent 30%, 40%, 50% of the amount of work that you ultimately do. In what you -- in ultimately creating a data-driven machine learning service. And so, data processing is just a massive part.

We accelerate Spark. We accelerate Python. One of the coolest things that we just did, it's called cuDF Pandas. Without one line of code, Pandas, which is the single most successful data science framework in the world, Pandas now is accelerated by NVIDIA CUDA and just out of the box without the line of code.

And so, the acceleration is really quite terrific. And people are just incredibly excited about. And Pandas was designed for one purpose and one purpose only really data processing for data science. And so, NVIDIA CUDA gives you all of that.

Gosh, you know, boy, that's just really excellent. You just wrote NVIDIA's business plan. And you described our strategy. First of all, there is a fundamental reason why we accelerate our execution.

And the reason for that is because it fundamentally drives down cost. When the combination of TensorRT LLM and 200 reduced the cost for our customers for large model inference by a factor of four. And so, that includes, of course, our speeds and feeds, but mostly it's because of our software, mostly the software benefits because of the architecture. And so, we want to accelerate our road map for that reason.

The second reason is to expand the reach of generative AI. The world's number of data center configurations, this is kind of the amazing thing. NVIDIA is in every cloud, but not one cloud is the same. NVIDIA is working with every single cloud service provider and not one of their networking control plane security posture is the same.

Everybody's platform is different. And yet we're integrated into all of their stacks, all of their data centers, and we work incredibly well with all of them. And not to mention, we didn't take the whole thing, and we create AI factories that are stand-alone. We take our platform.

We can put them into supercomputers. We can put them into enterprise. Bringing AI to enterprise is something generative AI to enterprise something nobody has ever done before. And we're right now in the process of going to market with all of that.

And so, the complexity includes, of course, all the technologies and segments and the pace, it includes the fact that we are architecturally compatible across every single one of those. And it's all of the domain-specific libraries that we create. The reason why you -- every computer company, without thinking, can integrate NVIDIA into their road map and take it to market, and the reason for that is because there's market demand for it. There's market demand and healthcare.

There's market demand in manufacturing, there's market demand, and of course, in AI, in financial services and supercomputing, and quantum computing. The list of markets and segments that we have domain-specific libraries is incredibly broad. And then finally, now we have an end-to-end solution for data centers. InfiniBand network, InfiniBand networking, Ethernet networking, x86 ARM, just about every permutation combination of solutions, technology solutions, and software stacks provided.

And that translates to having the largest number of ecosystem software developers, the largest ecosystem of system makers, the largest and broadest distribution partnership network, and ultimately, the greatest reach. And that takes – surely, that takes a lot of energy. But the thing that really holds together, and this is -- this is a great decision that we made decades ago, which is everything is architecturally compatible. When you -- when we develop a domain-specific language that runs on one GPU, it runs on every GPU.

When we optimize TensorRT for the cloud, we optimize it for enterprise. When we do something that brings in a new feature, a new library, a new feature, or a new developer, they instantly get the benefit of all of our reach. And so, that discipline, that architecture-compatible discipline that has lasted more than a couple of decades now is one of the reasons why NVIDIA is still really, really efficient. I mean, we're 28,000 people large and serving just about every single company, every single industry, every single market around the world.

Our strong growth reflects the broad industry platform transition from general-purpose to accelerated computing and Generative AI. Large language model start-ups, consumer Internet companies, and global cut service providers are the first movers. The next waves are starting to build. Nations and regional CSPs are building AI clouds to serve local demand.

Enterprise software companies like Adobe and Dropbox, SAP, and ServiceNow are adding AI copilots and assistants to their platforms. And enterprises in the world's largest industries are creating custom AIs to automate and boost productivity. The generative AI era is in full steam and has created the need for a new type of data center and AI factory, optimized for refining data and training and inference and generating AI. AI factory workloads are different and incremental to legacy data center workloads supporting IT tasks.

AI factories run copilots and AI assistants, which are significant software TAM expansion and are driving significant new investment, expanding the $1 trillion traditional data center infrastructure installed base, empowering the AI industrial revolution. NVIDIA H100 HGX with InfiniBand and the NVIDIA AI software stack defined an AI factory today. As we expand our supply chain to meet the world's demand, we are also building new growth drivers for the next wave of AI. We highlighted three elements to our new growth strategy that are hitting their stride, CPU, networking, and software and services.

Grace is NVIDIA first, data center CPU. Grace and Grace Hopper are in full production and ramping into a new multibillion-dollar product line next year, irrespective of the CPU choice. We can help customers build an AI factory. NVIDIA networking now exceeds a $10 billion annualized revenue run rate.

InfiniBand grew fivefold year over year and is positioned for excellent growth ahead as the networking of AI factories. Enterprises are also racing to adopt AI and Ethernet is the standard networking. This week, we announced an Ethernet for AI platform for enterprises. NVIDIA Spectrum X is an end-to-end solution of Bluefield Super Spectrum 4 Ethernet switch and software that boosts Ethernet performance by up to 1.6x for AI workloads.

Dell, HP, and Lenovo have joined us to bring a full generative AI solution of NVIDIA AI computing, networking, and software to the world's enterprises. NVIDIA Software and Services is on track to exit the year at an annualized run rate of $1 billion. Enterprise software platforms like ServiceNow and SAP need to build and operate proprietary AI. Enterprises need to build and deploy custom AI copilots.

We have the AI technology, expertise, and scale to help customers build custom models. With their proprietary data on NVIDIA DGX cloud and deploy the AI applications on enterprise-grade NVIDIA AI enterprise. NVIDIA is essentially an AI foundry. NVIDIA GPUs, CPUs, networking, AI foundry services, and NVIDIA AI enterprise software are all growth engines in full throttle.

Thanks for joining us today. We look forward to updating you on our progress next quarter.
