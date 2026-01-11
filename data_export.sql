--
-- PostgreSQL database dump
--

\restrict oP8EJnfwWDkNY72dyVi8K5AuvHbQYUyLwCu9Z1VWi1sIfytIlERDF51Na9xWslb

-- Dumped from database version 14.20 (Homebrew)
-- Dumped by pg_dump version 14.20 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: companies; Type: TABLE DATA; Schema: public; Owner: snitil
--

INSERT INTO public.companies VALUES (19, 'DRW', NULL);
INSERT INTO public.companies VALUES (20, 'Hunter Bond', 'https://www.hunterbond.com');
INSERT INTO public.companies VALUES (21, 'ALTEN Canada', NULL);
INSERT INTO public.companies VALUES (22, 'GIRO inc.', NULL);
INSERT INTO public.companies VALUES (23, 'Intact', 'https://www.intactfc.com');
INSERT INTO public.companies VALUES (24, 'Ericsson', 'https://www.ericsson.com');
INSERT INTO public.companies VALUES (25, 'Intelcom', 'https://intelcom.ca');
INSERT INTO public.companies VALUES (26, 'Boston Scientific', 'https://www.bostonscientific.com');
INSERT INTO public.companies VALUES (27, '0000050007 Royal Bank of Canada', NULL);
INSERT INTO public.companies VALUES (28, 'CSC Generation', 'https://www.cscgeneration.com');
INSERT INTO public.companies VALUES (29, 'Ericsson GmbH', 'https://www.ericsson.com');
INSERT INTO public.companies VALUES (30, 'WhatJobs Direct', 'https://www.whatjobs.com');
INSERT INTO public.companies VALUES (31, 'Safety CLI', 'https://docs.safetycli.com');
INSERT INTO public.companies VALUES (32, 'InterDigital, Inc.', 'https://www.interdigital.com');
INSERT INTO public.companies VALUES (33, 'Desjardins', 'https://www.desjardins.com');
INSERT INTO public.companies VALUES (34, 'Manulife', 'https://www.manulife.com');


--
-- Data for Name: jobs; Type: TABLE DATA; Schema: public; Owner: snitil
--

INSERT INTO public.jobs VALUES (13, 19, 'Software Developer Intern', 'Our formula for success is to hire exceptional people, encourage their ideas and reward their results.

As a Software Developer Intern, you will join one of our development teams supporting our network development initiatives or trading businesses. Depending on the team you join, you will build advanced trading, analysis and risk applications, or advanced monitoring and automation systems leveraging cutting-edge technology. DRW enables our Software Developer Interns to develop computationally intensive software under the guidance of senior technologists with the goal of deployment during your internship. While your days will have you immersed in complex projects directly driving DRW''s progress, your time also will be packed with education, responsibility, problem-solving, and social events to experience what it is like to work at DRW.

How will you make an impact?
• Design, develop test, and deploy proprietary software development solutions across the firm. Examples include

Creating
•', NULL, NULL, 'Montreal', NULL, 'https://ca.linkedin.com/jobs/view/software-developer-intern-at-drw-4354660803?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-06 14:38:49.525847');
INSERT INTO public.jobs VALUES (14, 20, 'C++ 20/23 Software Engineer (2-6 Years)- Up to $180k CAD + Bonus - Elite FinTech Firm', 'Job title: C++ 20/23 Software Engineer (2-6 Years)

Client: Elite FinTech Firm

Salary: Up to $180k CAD + Bonus

Location: Montreal (Hybrid Working)

Sells: Cutting-edge tech, ownership of multiple greenfield projects, no red tape, gold medal Olympiads, exceptional technologists, option to research and develop your own models, a friendly/collaborative environment, beautiful offices.

An Elite Tech Firm is looking for a highly talented C++ Software Engineer to join an elite group of individuals

This team have an unlimited tech budget, promote a great culture and are made up of fantastic like-minded technologists!

Role:

They’ll find the best team to suit your skillset/interests but you could be working on:

• Some of the world’s most performant ML pipelines that deal with millions of data points every second

• Building software solutions/products with scale, reliability and latency considerations in mind

Skills:
• 2-6 years of experience as a C++ Developer
• Strong knowledge of opti', 180000, 180000, 'Hybrid - Montreal', NULL, 'https://ca.linkedin.com/jobs/view/c%2B%2B-20-23-software-engineer-2-6-years-up-to-%24180k-cad-%2B-bonus-elite-fintech-firm-at-hunter-bond-4351182640?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-06 14:38:54.536129');
INSERT INTO public.jobs VALUES (15, 21, 'Développeur.se Nodejs', 'Développeur.se Node.js (Node.js Developer)

Qui sommes-nous ?

Chef de file mondial de l’industrie de l’ingénierie et du conseil TI avec plus de 58 000 conseiller·e·s à travers le monde, le Groupe ALTEN optimise la performance technologique des entreprises depuis plus de 30 ans.

Les personnes qui composent le groupe ALTEN constituent le moteur de notre activité. Chez ALTEN Canada, nous offrons à chaque candidat·e un service entièrement personnalisé. Vous avez la possibilité d’exercer votre métier de façon indépendante ou permanente. Nous sélectionnons les meilleures opportunités répondant à vos aspirations professionnelles. Nous positionnons votre savoir-faire sur des mandats passionnants à la hauteur de vos ambitions.

ALTEN Canada c’est aussi un centre de solutions, le « Montreal Delivery Center (MDC) », qui propose des services managés dans les domaines du développement applicatif, de la pratique Données, IA & Analytiques Avancées et de la Cyber Sécurité pour les secteurs bancaires', NULL, NULL, 'Montreal', NULL, 'https://ca.linkedin.com/jobs/view/d%C3%A9veloppeur-se-nodejs-at-alten-canada-4351411643?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-06 14:38:58.016485');
INSERT INTO public.jobs VALUES (16, 22, 'Summer 2026 - software development intern', 'GIRO IS YOUR WAY FORWARD

At GIRO, our mission is clear: Improving quality of life around the world through software and services that increase the efficiency of public transport and postal delivery.

Joining us means contributing to projects and initiatives that makes a real difference to millions of people. Every line of code, every idea, every action, advances our impact around the world. Join us and let’s lead the way forward, together.

Why choose GIRO?

• Join a Quebec software company that is an international leader

• Advance your career in a collaborative work environment where expertise and commitment are the driving force behind every project

• Stability based on long-lasting client relationships and our long-term vision

AN ENVIRONMENT FOR GROWTH

Here, we focus on an inclusive and positive environment.

We offer a range of benefits, including

• Flexible working hours, including remote work for a balanced life.

• Team activities and annual traditions that we take pride i', NULL, NULL, 'Montreal, Quebec', NULL, 'https://www.jobillico.com/en/job-offer/giro-inc/summer-2026-software-development-intern/16712316?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:36:22.613714');
INSERT INTO public.jobs VALUES (17, 23, 'Software Developer – 4 months Internship/Coop, Summer 2026', 'Our employees are at the heart of everything we do. Together, we help people, businesses, and society prosper in good times and be resilient in bad times.

Our employee promise represents Intact’s commitment to you in exchange for living our Values, striving to do your best work, being open to change and investing in your career. In return, we promise to provide support, opportunities and performance-led financial rewards at a workplace where you can shape the future, win as a team and grow with us.

Salary for the candidate will be determined taking into consideration a number of factors including: experience, skills, qualifications, anticipated contribution to role, internal equity, etc. The salary range presented below is based on a 35-hour workweek and would represent a majority of different candidate profiles. However, we encourage candidates who may fall outside of this range to apply as well.

Salary range (but not limited to):
61,500 - 76,900

About the role

Launching your tec', NULL, NULL, 'Montreal, Quebec', NULL, 'https://simplify.jobs/p/48f1110d-0c11-4767-b26e-05b7d315526d/Software-Developer--4-months-InternshipCoop?utm_source=GHList&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:36:22.697237');
INSERT INTO public.jobs VALUES (18, 24, 'Telecom IT Intern : Networking, Linux & Kubernetes', 'Un leader mondial des télécommunications basé à Montréal offre un stage de quatre mois en informatique. Les candidats doivent être inscrits à un programme de master ou licence en informatique ou dans un domaine technique pertinent. Le stage implique d''apprendre et d''expérimenter des solutions de télécommunications complexes en collaboration avec des mentors et des collègues. Une bonne connaissance des réseaux IP, des systèmes Unix et des compétences en scripting est requise. Ce poste ne propose pas de parrainage à l''immigration.

#J-18808-Ljbffr', NULL, NULL, 'Montreal, Quebec', NULL, 'https://ca.talent.com/view?id=3b483afdf769&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:36:22.848068');
INSERT INTO public.jobs VALUES (19, 25, 'Software Development Intern - GeoCoding', 'Make your internship count

At Intelcom, interns don''t just observe, they contribute meaningfully to real projects that shape how we operate. You''ll gain hands-on experience, grow your skills, and explore long-term career opportunities in a fast-moving, innovation-driven environment.

Ride the next mile with us!

We are seeking a Software Development Intern to support the implementation of Intelcom''s GeoCoding service. This is an exciting opportunity to apply your skills in a collaborative environment working on address coordination micro-services.

Responsibilities
• Participate in the development, testing, and maintenance of GeoCoding software services using Java.
• Collaborate to translate requirements into technical solutions.
• Write clean, efficient, and scalable code, along with comprehensive tests to ensure reliability and performance.
• Use CI/CD practices to build, test and deploy code changes.
• Participate in your team''s agile scrum sprints and ceremonies
• Participate in c', NULL, NULL, 'Montreal, Quebec', NULL, 'https://www.ziprecruiter.com/c/Intelcom/Job/Software-Development-Intern-GeoCoding/-in-Montreal,QC?jid=dd14fb4f7682d750&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:36:22.87182');
INSERT INTO public.jobs VALUES (20, 26, 'Software Development Intern / Stagiaire en développement de logiciels', 'Additional Location(s): Canada-QC-Montreal

Diversity - Innovation - Caring - Global Collaboration - Winning Spirit - High Performance

At Boston Scientific, we’ll give you the opportunity to harness all that’s within you by working in teams of diverse and high-performing employees, tackling some of the most important health industry challenges. With access to the latest tools, information and training, we’ll help you in advancing your skills and career. Here, you’ll be supported in progressing – whatever your ambitions.

Please note this is a 6-month contract opportunity beginning as soon as possible.

About the role

As a Software Development Intern, you''ll apply your technical skills to support the development and enhancement of software solutions. Working closely with our innovative engineering teams, you''ll contribute to coding, testing, and troubleshooting to improve system functionality. This role offers hands-on experience with key programming languages and the chance to collab', NULL, NULL, 'Montreal, Quebec', NULL, 'https://jobs.bostonscientific.com/job/Montreal-Software-Development-Intern-Stagiaire-en-d%C3%A9veloppement-de-logiciels-QC/1351385800/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:36:22.946411');
INSERT INTO public.jobs VALUES (21, 23, 'Software Developer – 4 months Internship/Coop', 'Our employees are at the heart of everything we do. Together, we help people, businesses, and society prosper in good times and be resilient in bad times.

Our employee promise represents Intact''s commitment to you in exchange for living our Values, striving to do your best work, being open to change and investing in your career. In return, we promise to provide support, opportunities and performance-led financial rewards at a workplace where you can shape the future, win as a team and grow with us.

Salary for the candidate will be determined taking into consideration a number of factors including: experience, skills, qualifications, anticipated contribution to role, internal equity, etc. The salary range presented below is based on a 35-hour workweek and would represent a majority of different candidate profiles. However, we encourage candidates who may fall outside of this range to apply as well.

Salary range (but not limited to):

61, ,900

About the role

Launching your tech care', NULL, NULL, 'Montreal, Quebec', NULL, 'https://ca.trabajo.org/job-3804-43d7e786588863fc10aeac9a5445776d?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:36:22.998796');
INSERT INTO public.jobs VALUES (22, 27, 'Summer Student RBC Borealis -Machine Learning Software Engineer Montreal', 'Position: 2026 Summer Student Opportunities RBC Borealis -Machine Learning Software Engineer, 4 Months - Montreal
Location: Montreal

Job Description
LOCATION: Montreal
What’s the opportunity?We’re looking for an enthusiastic software engineer who’s excited by the opportunity of being at the forefront of machine learning technology, and working on extremely challenging problems. As a Co-op Machine Learning Software Engineer
, you’ll be involved a project end to end – everything from data pre-processing to implementing machine learning algorithms and front-end development.

At RBC Borealis, you’ll be joining a team that works directly with leading researchers in machine learning, has access to rich and massive datasets, and offers the computational resources to support ongoing development in areas such as reinforcement learning, unsupervised learning and computer vision. You can find out more about our research areas at Your responsibilities include:
• Building machine learning-based so', NULL, NULL, 'Montreal, Quebec', NULL, 'https://www.learn4good.com/jobs/montreal/canada/info_technology/4773705551/e/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:36:23.099129');
INSERT INTO public.jobs VALUES (23, 25, 'Software Development Intern - Mobile Application', 'Make your internship count

At Intelcom, interns don''t just observe, they contribute meaningfully to real projects that shape how we operate. You''ll gain hands-on experience, grow your skills, and explore long-term career opportunities in a fast-moving, innovation-driven environment.

Ride the next mile with us!

We are seeking a Software Development Intern to join our Mobile Application team to enhance driver experience. This is an exciting opportunity to gain hands-on experience in building and enhancing mobile system functionality and efficiency.

Responsibilities
• Participate in the development, testing and maintenance of the Route Application using MAUI.net (C#)
• Collaborate with the operations department to translate requirements into technical solutions aligned with driver''s needs and operational workflows
• Build proofs of concepts (POCs) for mobile application
• Write clean, efficient and scalable code
• Participate in code reviews and provide constructive feedback
• Contrib', NULL, NULL, 'Montreal, Quebec', NULL, 'https://www.ziprecruiter.com/c/Intelcom/Job/Software-Development-Intern-Mobile-Application/-in-Montreal,QC?jid=9eb4b37c1d43d777&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:36:23.184029');
INSERT INTO public.jobs VALUES (24, 28, 'Junior Software Engineer (Full Stack, React and Node)', 'CSC Generation is a technology driven holding company that acquires and operates established consumer brands, including One Kings Lane, Backcountry, and Sur La Table. Across 13 brands generating over $1B in annual revenue, we improve how these businesses run by building shared platforms, automation, and data tooling that scale across the portfolio.

This role is platform work at the intersection of e-commerce, operations, and data. You will ship production changes used daily, and you will learn reliable delivery through small pull requests, code review, and disciplined debugging.

This Junior Software Engineer role is for early career full-stack engineers who want to grow quickly. You will work primarily in JavaScript and TypeScript, with React on the front end and Node on the back end, and over time you will own small features end to end.

What you get to do:
• Build and refine user facing features using React, TypeScript, and modernfront endtooling.
• Implement and integrate simple b', NULL, NULL, 'Montreal, Quebec', NULL, 'https://www.recruit.net/job/software-engineer-full-stack-react-jobs/BC1179902FDAB9E3?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:36:23.235459');
INSERT INTO public.jobs VALUES (25, 29, 'Software Developer Intern – Cloud & 5G Microservices (Montreal)', 'Une entreprise technologique internationale basée à Montréal recherche un stagiaire développeur de logiciels pour rejoindre une équipe innovante. Vous serez impliqué dans l''amélioration du cadre de surveillance des tests et contribuerez à la création de tests automatisés. Les candidats doivent avoir des connaissances en Java et JavaScript ainsi que de bonnes compétences en communication. Ce stage est une excellente opportunité pour les étudiants en ingénierie ou en informatique.
#J-18808-Ljbffr', NULL, NULL, 'Montreal, Quebec', NULL, 'https://www.recruit.net/job/software-developer-cloud-g-microservices-jobs/6C1D1EB86A0D1315?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:41:41.271172');
INSERT INTO public.jobs VALUES (26, 30, 'Apprentice Software Developer', 'Our client is excited to offer a unique Apprenticeship program for aspiring Software Developers. This is a fully remote, immersive learning experience designed to equip individuals with the foundational skills and practical knowledge needed to excel in the tech industry. You will be paired with experienced mentors who will guide you through coding best practices, software development lifecycle, and various programming languages. This role is perfect for individuals with a passion for technology, a strong aptitude for problem-solving, and a desire to build a career in software development, all from the comfort of your home office. As a remote-first program, we leverage cutting-edge collaboration tools to ensure a connected and productive environment.

Program Highlights: Hands-on training in modern programming languages (e.g., Python, JavaScript, Java). Exposure to full-stack development, including front-end and back-end technologies. Learning industry-standard development tools and met', NULL, NULL, 'Montreal, Quebec', NULL, 'https://en-ca.whatjobs.com/jobs/apprentice-software-developer?id=100962469&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:41:41.327848');
INSERT INTO public.jobs VALUES (27, 31, 'Co-op: Developer Tools Engineer', 'Safety Cybersecurity is dedicated to helping development teams build and deploy secure applications with confidence. Our cutting-edge platform integrates seamlessly into the development workflow, providing real-time vulnerability detection and actionable remediation guidance. We are focused on building the world’s first AI-powered software supply chain firewall.

The Opportunity

We''re looking for a motivated Computer Science student, including those participating in the Venture For Canada summer intern program, to join our Product team for a co-op position. As a Developer Tools Engineer intern, you''ll have the exciting opportunity to work on extending our platform''s capabilities to support various Integrated Development Environments (IDEs). This role offers hands-on experience in a fast-paced cybersecurity environment where you''ll contribute directly to our product''s evolution.

What You’ll Do
• Design and implement IDE extensions that integrate the Safety platform into developers’ pr', NULL, NULL, 'Montreal, Quebec', NULL, 'https://www.recruit.net/job/co-op-developer-tools-engineer-jobs/9172EB1D98A22F87?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:41:41.381941');
INSERT INTO public.jobs VALUES (28, 32, 'Intern, Screen Content tools for Video Compression/Coding', 'About InterDigital

InterDigital is a global research and development company focused primarily on wireless, video, artificial intelligence (“AI”), and related technologies. We design and develop foundational technologies that enable connected, immersive experiences in a broad range of communications and entertainment products and services. We license our innovations worldwide to companies providing such products and services, including makers of wireless communications devices, consumer electronics, IoT devices, cars and other motor vehicles, and providers of cloud-based services such as video streaming. As a leader in wireless technology, our engineers have designed and developed a wide range of innovations that are used in wireless products and networks, from the earliest digital cellular systems to 5G and today’s most advanced Wi-Fi technologies. We are also a leader in video processing and video encoding/decoding technology, with a significant AI research effort that intersects wi', NULL, NULL, 'Montreal, Quebec', NULL, 'https://ca.linkedin.com/jobs/view/intern-screen-content-tools-for-video-compression-coding-at-interdigital-inc-4315880139?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:41:41.434261');
INSERT INTO public.jobs VALUES (29, 30, 'Junior Software Developer - Apprenticeship Program, Remote', 'Our client, a dynamic and rapidly expanding software development company, is excited to offer a unique Junior Software Developer opportunity through their fully remote Apprenticeship Program. This is an ideal entry-level position for aspiring developers eager to launch their careers in the tech industry. As an apprentice, you will receive hands-on training and mentorship from experienced engineers, working on real-world projects and gaining invaluable practical experience. You will learn to write, test, and debug code, collaborate with team members on software design and architecture, and contribute to the development of innovative applications. The curriculum is designed to provide a comprehensive understanding of software development principles, programming languages (e.g., Python, Java, JavaScript), and modern development tools and practices. This fully remote program allows you to learn and grow from the comfort of your home office, eliminating the need for relocation or daily comm', NULL, NULL, 'Montreal, Quebec', NULL, 'https://en-ca.whatjobs.com/jobs/developer?id=100960067&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:41:41.49864');
INSERT INTO public.jobs VALUES (30, 30, 'Graduate Software Developer (AI Focus)', 'Our client is offering an exciting Graduate Software Developer internship opportunity with a focus on Artificial Intelligence and Machine Learning. This is a fully remote role, allowing aspiring tech professionals to gain invaluable industry experience from anywhere in Canada. You will work alongside seasoned engineers on cutting-edge AI projects, contributing to the development of intelligent systems and algorithms. This internship is designed for motivated individuals seeking to launch their career in a challenging and rewarding environment, applying theoretical knowledge to real-world problems.

Responsibilities:
Assist in the design, development, and implementation of AI/ML models and algorithms. Write clean, efficient, and well-documented code in languages such as Python, Java, or C++. Collaborate with senior developers and researchers on AI research projects. Collect, clean, and preprocess data for training machine learning models. Participate in code reviews and contribute to im', NULL, NULL, 'Montreal, Quebec', NULL, 'https://en-ca.whatjobs.com/jobs/deep-learning?id=100928505&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:41:41.549992');
INSERT INTO public.jobs VALUES (31, 33, 'Internship, IT sector, Summer 2026', '💚 Are You Looking For a One-of-kind Experience With An Outstanding Team In a Modern Environment? We’re Looking For Bright Interns Who Like To Learn Because With Our Squads, There’s Always Something New. Starting Your Career At Quebec’s Largest Private IT Employer, (we Have More Than 9,000 IT Employees!) Is An Opportunity Not To Be Missed. Desjardins Is a Top Employer That’s Committed To The Next Generation Of IT Professionals. There Are Several Internship Positions Available. More Specifically, We’re Looking For

📊Business administration intern
• Analyze issues related to your line of work, conduct research and preliminary analysis, develop initial outlines for tools and working processes, and draw on your comprehensive knowledge of the business segment while acting as an advisor to our dedicated clients and partners.

📐Operations systems analysis intern
• Implement the infrastructure in accordance with architectural specifications and operating standards, while contributing to the rel', NULL, NULL, 'Montreal West, Quebec', NULL, 'https://ca.linkedin.com/jobs/view/internship-it-sector-summer-2026-at-desjardins-4351795810?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:50:56.263507');
INSERT INTO public.jobs VALUES (32, 33, 'Internship, IT sector, Summer 2026', 'Are you looking for a one-of-kind experience with an outstanding team in a modern environment? We’re looking for bright interns who like to learn because with our squads, there’s always something new. Starting your career at Quebec’s largest private IT employer, (we have more than 9,000 IT employees!) is an opportunity not to be missed. Desjardins is a top employer that’s committed to the next generation of IT professionals. There are several internship positions available. More specifically, we’re looking for:

Business administration intern
• Analyze issues related to your line of work, conduct research and preliminary analysis, develop initial outlines for tools and working processes, and draw on your comprehensive knowledge of the business segment while acting as an advisor to our dedicated clients and partners.

Operations systems analysis intern
• Implement the infrastructure in accordance with architectural specifications and operating standards, while contributing to the reliab', NULL, NULL, 'Montreal, Quebec', NULL, 'https://ca.indeed.com/viewjob?jk=9bfcf770aef1c3b6&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:50:56.296525');
INSERT INTO public.jobs VALUES (33, 34, 'Summer Intern/Co-op 2026  Communications / Design', 'Join our Global Cybersecurity (GCS) Team as a Communications & Design Intern and play a key role in centralizing resources, supporting internal campaigns, and creating branded assets that align with Manulife’s standards. This role combines creativity, technology, and collaboration to deliver impactful solutions.

Position Responsibilities:
• Design and develop a SharePoint site to centralize GCS resources and updates.
• Create branded templates and visual assets aligned with Manulife’s brand standards.
• Support internal communication campaigns and culture initiatives.
• Coordinate 2026 cybersecurity training sessions with vendors and internal stakeholders.
• Assist with day-to-day administrative and creative tasks to enable strategic priorities.
• Collaborate with cybersecurity and communications teams to deliver high-quality content.

Required Qualifications:
• Currently pursuing an undergraduate degree in Communications, Graphic Design, Digital Media, Marketing, Information Technolo', NULL, NULL, 'Montreal, Quebec', NULL, 'https://grabjobs.co/canada/job/internship/others/summer-interncoop-2026-communications-and-design-152263674?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', '2026-01-11 09:50:56.666151');


--
-- Data for Name: skills; Type: TABLE DATA; Schema: public; Owner: snitil
--

INSERT INTO public.skills VALUES (22, 'Python');
INSERT INTO public.skills VALUES (23, 'JavaScript');
INSERT INTO public.skills VALUES (24, 'Node.js');
INSERT INTO public.skills VALUES (25, 'React');
INSERT INTO public.skills VALUES (26, 'Angular');
INSERT INTO public.skills VALUES (27, 'C++');
INSERT INTO public.skills VALUES (28, 'Ruby');
INSERT INTO public.skills VALUES (29, 'C#');
INSERT INTO public.skills VALUES (30, 'Go');
INSERT INTO public.skills VALUES (31, 'Java');
INSERT INTO public.skills VALUES (32, 'ML pipelines');
INSERT INTO public.skills VALUES (33, 'optimization');
INSERT INTO public.skills VALUES (34, 'performance');
INSERT INTO public.skills VALUES (35, 'Rust');
INSERT INTO public.skills VALUES (36, 'TypeScript');
INSERT INTO public.skills VALUES (37, 'REST APIs');
INSERT INTO public.skills VALUES (38, 'Git');
INSERT INTO public.skills VALUES (39, 'Swagger');
INSERT INTO public.skills VALUES (40, 'OpenAPI');
INSERT INTO public.skills VALUES (41, 'SQL');
INSERT INTO public.skills VALUES (42, 'NoSQL');
INSERT INTO public.skills VALUES (43, 'Agile');
INSERT INTO public.skills VALUES (44, 'AWS');
INSERT INTO public.skills VALUES (45, 'Docker');
INSERT INTO public.skills VALUES (46, 'Kubernetes');
INSERT INTO public.skills VALUES (47, 'MongoDB');
INSERT INTO public.skills VALUES (48, 'Kotlin');
INSERT INTO public.skills VALUES (49, 'REST');
INSERT INTO public.skills VALUES (50, 'Kafka');
INSERT INTO public.skills VALUES (51, 'RabbitMQ');
INSERT INTO public.skills VALUES (52, 'CI/CD');
INSERT INTO public.skills VALUES (53, 'Azure');
INSERT INTO public.skills VALUES (54, 'Machine Learning');
INSERT INTO public.skills VALUES (55, 'Spark');
INSERT INTO public.skills VALUES (56, 'Hadoop');
INSERT INTO public.skills VALUES (57, 'Bash');
INSERT INTO public.skills VALUES (58, 'Express');
INSERT INTO public.skills VALUES (59, 'Shell');
INSERT INTO public.skills VALUES (60, 'Data Science');


--
-- Data for Name: job_skills; Type: TABLE DATA; Schema: public; Owner: snitil
--

INSERT INTO public.job_skills VALUES (13, 22);
INSERT INTO public.job_skills VALUES (13, 23);
INSERT INTO public.job_skills VALUES (13, 24);
INSERT INTO public.job_skills VALUES (13, 25);
INSERT INTO public.job_skills VALUES (13, 26);
INSERT INTO public.job_skills VALUES (13, 27);
INSERT INTO public.job_skills VALUES (13, 28);
INSERT INTO public.job_skills VALUES (13, 29);
INSERT INTO public.job_skills VALUES (13, 30);
INSERT INTO public.job_skills VALUES (13, 31);
INSERT INTO public.job_skills VALUES (14, 27);
INSERT INTO public.job_skills VALUES (14, 32);
INSERT INTO public.job_skills VALUES (14, 33);
INSERT INTO public.job_skills VALUES (14, 34);
INSERT INTO public.job_skills VALUES (14, 35);
INSERT INTO public.job_skills VALUES (15, 24);
INSERT INTO public.job_skills VALUES (15, 36);
INSERT INTO public.job_skills VALUES (15, 37);
INSERT INTO public.job_skills VALUES (15, 38);
INSERT INTO public.job_skills VALUES (15, 39);
INSERT INTO public.job_skills VALUES (15, 40);
INSERT INTO public.job_skills VALUES (15, 41);
INSERT INTO public.job_skills VALUES (15, 42);
INSERT INTO public.job_skills VALUES (16, 43);
INSERT INTO public.job_skills VALUES (17, 31);
INSERT INTO public.job_skills VALUES (17, 25);
INSERT INTO public.job_skills VALUES (17, 44);
INSERT INTO public.job_skills VALUES (17, 45);
INSERT INTO public.job_skills VALUES (17, 46);
INSERT INTO public.job_skills VALUES (17, 47);
INSERT INTO public.job_skills VALUES (17, 38);
INSERT INTO public.job_skills VALUES (17, 36);
INSERT INTO public.job_skills VALUES (17, 30);
INSERT INTO public.job_skills VALUES (17, 48);
INSERT INTO public.job_skills VALUES (17, 26);
INSERT INTO public.job_skills VALUES (17, 49);
INSERT INTO public.job_skills VALUES (17, 50);
INSERT INTO public.job_skills VALUES (17, 51);
INSERT INTO public.job_skills VALUES (19, 31);
INSERT INTO public.job_skills VALUES (19, 44);
INSERT INTO public.job_skills VALUES (19, 29);
INSERT INTO public.job_skills VALUES (19, 30);
INSERT INTO public.job_skills VALUES (19, 52);
INSERT INTO public.job_skills VALUES (19, 43);
INSERT INTO public.job_skills VALUES (19, 53);
INSERT INTO public.job_skills VALUES (20, 22);
INSERT INTO public.job_skills VALUES (20, 31);
INSERT INTO public.job_skills VALUES (20, 38);
INSERT INTO public.job_skills VALUES (20, 27);
INSERT INTO public.job_skills VALUES (20, 30);
INSERT INTO public.job_skills VALUES (21, 31);
INSERT INTO public.job_skills VALUES (21, 25);
INSERT INTO public.job_skills VALUES (21, 44);
INSERT INTO public.job_skills VALUES (21, 45);
INSERT INTO public.job_skills VALUES (21, 46);
INSERT INTO public.job_skills VALUES (21, 47);
INSERT INTO public.job_skills VALUES (21, 38);
INSERT INTO public.job_skills VALUES (21, 36);
INSERT INTO public.job_skills VALUES (21, 30);
INSERT INTO public.job_skills VALUES (21, 48);
INSERT INTO public.job_skills VALUES (21, 26);
INSERT INTO public.job_skills VALUES (21, 49);
INSERT INTO public.job_skills VALUES (21, 50);
INSERT INTO public.job_skills VALUES (21, 51);
INSERT INTO public.job_skills VALUES (22, 22);
INSERT INTO public.job_skills VALUES (22, 31);
INSERT INTO public.job_skills VALUES (22, 41);
INSERT INTO public.job_skills VALUES (22, 27);
INSERT INTO public.job_skills VALUES (22, 29);
INSERT INTO public.job_skills VALUES (22, 30);
INSERT INTO public.job_skills VALUES (22, 54);
INSERT INTO public.job_skills VALUES (22, 55);
INSERT INTO public.job_skills VALUES (22, 56);
INSERT INTO public.job_skills VALUES (22, 57);
INSERT INTO public.job_skills VALUES (23, 22);
INSERT INTO public.job_skills VALUES (23, 23);
INSERT INTO public.job_skills VALUES (23, 31);
INSERT INTO public.job_skills VALUES (23, 29);
INSERT INTO public.job_skills VALUES (23, 30);
INSERT INTO public.job_skills VALUES (24, 23);
INSERT INTO public.job_skills VALUES (24, 31);
INSERT INTO public.job_skills VALUES (24, 25);
INSERT INTO public.job_skills VALUES (24, 44);
INSERT INTO public.job_skills VALUES (24, 38);
INSERT INTO public.job_skills VALUES (24, 36);
INSERT INTO public.job_skills VALUES (24, 30);
INSERT INTO public.job_skills VALUES (24, 58);
INSERT INTO public.job_skills VALUES (24, 49);
INSERT INTO public.job_skills VALUES (25, 23);
INSERT INTO public.job_skills VALUES (25, 31);
INSERT INTO public.job_skills VALUES (26, 22);
INSERT INTO public.job_skills VALUES (26, 23);
INSERT INTO public.job_skills VALUES (26, 31);
INSERT INTO public.job_skills VALUES (26, 38);
INSERT INTO public.job_skills VALUES (26, 43);
INSERT INTO public.job_skills VALUES (27, 22);
INSERT INTO public.job_skills VALUES (27, 38);
INSERT INTO public.job_skills VALUES (27, 52);
INSERT INTO public.job_skills VALUES (27, 49);
INSERT INTO public.job_skills VALUES (28, 22);
INSERT INTO public.job_skills VALUES (28, 38);
INSERT INTO public.job_skills VALUES (28, 27);
INSERT INTO public.job_skills VALUES (28, 30);
INSERT INTO public.job_skills VALUES (28, 58);
INSERT INTO public.job_skills VALUES (28, 59);
INSERT INTO public.job_skills VALUES (29, 22);
INSERT INTO public.job_skills VALUES (29, 23);
INSERT INTO public.job_skills VALUES (29, 31);
INSERT INTO public.job_skills VALUES (29, 43);
INSERT INTO public.job_skills VALUES (29, 49);
INSERT INTO public.job_skills VALUES (30, 22);
INSERT INTO public.job_skills VALUES (30, 31);
INSERT INTO public.job_skills VALUES (30, 27);
INSERT INTO public.job_skills VALUES (30, 30);
INSERT INTO public.job_skills VALUES (30, 54);
INSERT INTO public.job_skills VALUES (30, 60);
INSERT INTO public.job_skills VALUES (30, 43);
INSERT INTO public.job_skills VALUES (31, 30);
INSERT INTO public.job_skills VALUES (32, 30);
INSERT INTO public.job_skills VALUES (33, 44);
INSERT INTO public.job_skills VALUES (33, 38);
INSERT INTO public.job_skills VALUES (33, 58);
INSERT INTO public.job_skills VALUES (33, 49);


--
-- Data for Name: raw_postings; Type: TABLE DATA; Schema: public; Owner: snitil
--

INSERT INTO public.raw_postings VALUES (7, 'jsearch', 'https://ca.linkedin.com/jobs/view/software-developer-intern-at-drw-4354660803?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Software Developer Intern
Company: DRW
Location: Montreal, Quebec CA
Employment Type: Full-time
Posted: 2026-01-05T20:00:00.000Z

Salary: Not specified

Description:
Our formula for success is to hire exceptional people, encourage their ideas and reward their results.

As a Software Developer Intern, you will join one of our development teams supporting our network development initiatives or trading businesses. Depending on the team you join, you will build advanced trading, analysis and risk applications, or advanced monitoring and automation systems leveraging cutting-edge technology. DRW enables our Software Developer Interns to develop computationally intensive software under the guidance of senior technologists with the goal of deployment during your internship. While your days will have you immersed in complex projects directly driving DRW''s progress, your time also will be packed with education, responsibility, problem-solving, and social events to experience what it is like to work at DRW.

How will you make an impact?
• Design, develop test, and deploy proprietary software development solutions across the firm. Examples include

Creating
• MLOps and High Availability inference systems
• Data pipeline engineering
• Agentic / RAG / MCP(tools) Development
• GPU optimization and management
• Full stack web applications and dashboards
• Identify innovative solutions to complex problems and advocate for their implementation to your team by communicating your ideas in a clear and concise manner
• Conduct research using a data driven approach to employ statistical analytics on large data sets
• Collaborate with other software developers, quantitative traders and researchers as well as business analysts in cross-functional team environments

What do you bring to the team?
• Are pursuing a bachelor''s, master''s, or PhD in computer science, electrical engineering, computer engineering, physics, mathematics or any related science discipline and have an expected graduation date between December 2026 and June 2027
• Have exposure to multi-threaded applications, computational intelligence, algorithms, real-time programming or GUI programming
• Have strong understanding of object-oriented design, data structures, and algorithms
• Exhibit excellent software development skills in at least one of Python, JavaScript (Node, React, and/or Angular), C++, Ruby, C#, Go or Java, and a deep curiosity to learn and absorb new technologies quickly

What to expect during the internship?
• Meaningful projects: You''ll receive a challenging project to complete during your time here. Each project, advised by a software engineer, promotes a comprehensive learning experience and provides you with meaningful work experience.
• Community: Throughout the summer, we host a variety of educational, social and team-building activities to foster friendship and camaraderie.
• Housing: DRW provides fully furnished apartments located close to the office making your morning commute as easy as possible.
• Mentorship: You''ll build a professional relationship with an experienced mentor in your field. Mentors and mentees meet to discuss goals, challenges and professional development and explore the city together at our mentor outings.
• Education: As the trading industry continually evolves, both in terms of new products and transaction methods, the future will present us with unique opportunities and challenges. You’ll complete an options course taught by an experienced trader and participate in a technology immersion course to better understand how technology and trading intersect.

DRW is a diversified trading firm with over 3 decades of experience bringing sophisticated technology and exceptional people together to operate in markets around the world. We value autonomy and the ability to quickly pivot to capture opportunities, so we operate using our own capital and trading at our own risk.

Headquartered in Chicago with offices throughout the U.S., Canada, Europe, and Asia, we trade a variety of asset classes including Fixed Income, ETFs, Equities, FX, Commodities and Energy across all major global markets. We have also leveraged our expertise and technology to expand into three non-traditional strategies: real estate, venture capital and cryptoassets.

We operate with respect, curiosity and open minds. The people who thrive here share our belief that it’s not just what we do that matters–it''s how we do it. DRW is a place of high expectations, integrity, innovation and a willingness to challenge consensus.

For more information about DRW''s processing activities and our use of job applicants'' data, please view our Privacy Notice at https://drw.com/privacy-notice.

California residents, please review the California Privacy Notice for information about certain legal rights at https://drw.com/california-privacy-notice.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-06 14:38:41.928644', true, 13);
INSERT INTO public.raw_postings VALUES (8, 'jsearch', 'https://ca.linkedin.com/jobs/view/c%2B%2B-20-23-software-engineer-2-6-years-up-to-%24180k-cad-%2B-bonus-elite-fintech-firm-at-hunter-bond-4351182640?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: C++ 20/23 Software Engineer (2-6 Years)- Up to $180k CAD + Bonus - Elite FinTech Firm
Company: Hunter Bond
Location: Montreal, Quebec CA
Employment Type: Full-time
Posted: 2026-01-04T00:00:00.000Z

Salary: Not specified

Description:
Job title: C++ 20/23 Software Engineer (2-6 Years)

Client: Elite FinTech Firm

Salary: Up to $180k CAD + Bonus

Location: Montreal (Hybrid Working)

Sells: Cutting-edge tech, ownership of multiple greenfield projects, no red tape, gold medal Olympiads, exceptional technologists, option to research and develop your own models, a friendly/collaborative environment, beautiful offices.

An Elite Tech Firm is looking for a highly talented C++ Software Engineer to join an elite group of individuals

This team have an unlimited tech budget, promote a great culture and are made up of fantastic like-minded technologists!

Role:

They’ll find the best team to suit your skillset/interests but you could be working on:

• Some of the world’s most performant ML pipelines that deal with millions of data points every second

• Building software solutions/products with scale, reliability and latency considerations in mind

Skills:
• 2-6 years of experience as a C++ Developer
• Strong knowledge of optimization/performance
• An interest in Rust is a nice plus
• Experience working at a large scale scale

Required Skills/Qualifications:
[''Not specified'']', '2026-01-06 14:38:49.676074', true, 14);
INSERT INTO public.raw_postings VALUES (9, 'jsearch', 'https://ca.linkedin.com/jobs/view/d%C3%A9veloppeur-se-nodejs-at-alten-canada-4351411643?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Développeur.se Nodejs
Company: ALTEN Canada
Location: Montreal, Quebec CA
Employment Type: Full-time
Posted: 2026-01-06T16:00:00.000Z

Salary: Not specified

Description:
Développeur.se Node.js (Node.js Developer)

Qui sommes-nous ?

Chef de file mondial de l’industrie de l’ingénierie et du conseil TI avec plus de 58 000 conseiller·e·s à travers le monde, le Groupe ALTEN optimise la performance technologique des entreprises depuis plus de 30 ans.

Les personnes qui composent le groupe ALTEN constituent le moteur de notre activité. Chez ALTEN Canada, nous offrons à chaque candidat·e un service entièrement personnalisé. Vous avez la possibilité d’exercer votre métier de façon indépendante ou permanente. Nous sélectionnons les meilleures opportunités répondant à vos aspirations professionnelles. Nous positionnons votre savoir-faire sur des mandats passionnants à la hauteur de vos ambitions.

ALTEN Canada c’est aussi un centre de solutions, le « Montreal Delivery Center (MDC) », qui propose des services managés dans les domaines du développement applicatif, de la pratique Données, IA & Analytiques Avancées et de la Cyber Sécurité pour les secteurs bancaires, télécoms et pour l’industrie au sens large.

Nos expert·e·s sont sélectionné·e·s rigoureusement et assurent une proximité ainsi qu’un niveau de services et de compétences incomparable dans la région de Montréal.

Quels profils recrutons-nous et pour qui ?

Pour soutenir la croissance de notre client dans le secteur bancaire, ALTEN Canada recrute un.e

Développeur/Développeuse Node.js dont le rôle sera de développer et faire évoluer des services backend et des API.

Quelles seront mes responsabilités ?
• Analyser les besoins et proposer des solutions techniques simples et efficaces
• Concevoir, développer et maintenir des API REST et services backend en Node.js
• Participer à la qualité : revues de code, documentation, bonnes pratiques
• Développer avec des tests automatisés (unitaires / intégration)
• Assurer la stabilité et la sécurité des applications (correctifs, amélioration continue)

Je suis convaincu-e ! Quelles compétences dois-je avoir pour rejoindre vos équipes ?
• 4 ans d’expérience pertinente en développement backend
• Expérience solide en Node.js (TypeScript est un atout)
• Expérience en API REST (développement et intégration)
• À l’aise avec des outils modernes : Git, documentation d’API (Swagger/OpenAPI ou équivalent)
• Notions de bases de données SQL ou NoSQL (atout)
• Maîtrise de la langue française, car il y aura beaucoup d’interactions avec des partenaires locaux (anglais est un atout)

Pourquoi se joindre à nos équipes?

Alten Canada offre un environnement de travail dynamique et collaboratif. Nous offrons aux membres de notre équipe l’occasion de vivre des expériences stimulantes et nous investissons dans leur perfectionnement et leur développement professionnels.

Parmi nos avantages :

Rémunération et avantages sur mesure pour chacun de nos employé.e.s et pigistes ;

Aide perfectionnement professionnel (certification) ;

Possibilité de mobilité internationale dans l’une des filiales du Groupe ;

Nombreuses activités corporatives ;

Veuillez noter que toutes les demandes seront évaluées, toutefois, nous ne communiquerons qu’avec les candidat.e.s sélectionné.e.s dans le cadre de cette offre d’emploi.

ALTEN Canada s''engage à promouvoir l''équité, la diversité et l''inclusion. Nous nous engageons à offrir un environnement de travail où chaque personne se sente accueillie, valorisée et respectée afin de pouvoir s’épanouir pleinement.

Nous avons à cœur d’offrir des mesures d’accessibilité aux personnes qui en font la demande, à ce titre, nous vous encourageons à communiquer avec nous si vous avez besoin d’accommodation dans le cadre du processus de recrutement.

Who are we?

A global leader in the engineering and IT consulting industry with over 58,000 consultants worldwide, the ALTEN Group has been optimizing the technological performance of companies for over 30 years.

The individuals who make up the ALTEN Group are the driving force behind our activity. At ALTEN Canada, we offer each candidate a fully personalized service. You have the option to work independently or permanently. We select the best opportunities that match your professional aspirations. We position your expertise on exciting projects that meet your ambitions.

ALTEN Canada is also a solutions center, the "Montreal Delivery Center (MDC)", which offers managed services in the fields of application development, Data, AI & Advanced Analytics practice, and Cyber Security for the banking, telecom sectors, and industry at large.

Our experts are rigorously selected and ensure proximity as well as an unparalleled level of service and expertise in the Montreal area.

What profiles are we recruiting and for whom?

To support the growth of our banking client, ALTEN Canada is recruiting a Node.js Developer whose role will be to build and maintain backend services and REST APIs.

What will be my responsibilities?
• Understand requirements and propose simple, pragmatic technical solutions
• Design, build, and maintain REST APIs and backend services using Node.js
• Contribute to delivery quality: code reviews, documentation, best practices
• Build with automated tests (unit/integration)
• Ensure application stability and security (fixes, continuous improvement)

I''m convinced! What skills do I need to join your teams?
• 4+ years of relevant experience in backend development
• Strong Node.js experience (TypeScript is a plus)
• Experience building/maintaining REST APIs
• Comfortable with modern tools: Git, API documentation (Swagger/OpenAPI or equivalent)
• Knowledge of SQL or NoSQL databases (nice to have)
• French required, due to frequent interactions with local partners (English is a plus)

Why join our teams?

Alten Canada offers a dynamic and collaborative work environment. We provide our team members with the opportunity to have stimulating experiences and invest in their professional development.

Among our benefits:

Customized compensation and benefits for each of our employees and freelancers;

Professional development assistance (certification);

Possibility of international mobility in one of the Group''s subsidiaries;

Numerous corporate activities.

Please note that all applications will be reviewed; however, we will only contact the selected candidates for this job offer.

ALTEN CANADA is committed to promoting diversity, equity, and inclusion. We strive to provide a work environment where every individual feels welcomed, valued, and respected, allowing them to thrive to their full potential. This includes our dedication to offer accessibility measures to those who require them. Should you require any accommodation during our recruitment process, please reach out to us.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-06 14:38:54.619687', true, 15);
INSERT INTO public.raw_postings VALUES (10, 'jsearch', 'https://www.jobillico.com/en/job-offer/giro-inc/summer-2026-software-development-intern/16712316?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Summer 2026 - software development intern
Company: GIRO inc.
Location: Montreal, Quebec CA
Employment Type: Internship
Posted: 2026-01-05T00:00:00.000Z

Salary: Not specified

Description:
GIRO IS YOUR WAY FORWARD

At GIRO, our mission is clear: Improving quality of life around the world through software and services that increase the efficiency of public transport and postal delivery.

Joining us means contributing to projects and initiatives that makes a real difference to millions of people. Every line of code, every idea, every action, advances our impact around the world. Join us and let’s lead the way forward, together.

Why choose GIRO?

• Join a Quebec software company that is an international leader

• Advance your career in a collaborative work environment where expertise and commitment are the driving force behind every project

• Stability based on long-lasting client relationships and our long-term vision

AN ENVIRONMENT FOR GROWTH

Here, we focus on an inclusive and positive environment.

We offer a range of benefits, including

• Flexible working hours, including remote work for a balanced life.

• Team activities and annual traditions that we take pride in

• Everyday support: Employee assistance program, telemedicine and mental health support.

• Training and professional development opportunities to grow, learn and discover your way forward.

HOW YOU’LL MAKE A POSITIVE IMPACT

GIRO is looking for several software development interns for the Fall 2025 term. At GIRO, you''ll be an integral part of a development team and collaborate with software experts who have deep expertise in public transit and postal services. Come grow and learn with us! And who knows? You might just fall in love with our field and want to start your career here ?

In addition to discovering how to work in an agile environment, a development internship at GIRO means:
• Participating in the design and development stages of a large-scale software product suite: functional design, architecture, detailed analysis, and programming;
• Developing new features in applications;
• Implementing and testing software functionalities;
• Managing bugs (OBS) and finding appropriate solutions to fix them.

Your internship will also involve:
• Providing technical support to development and project teams using the features developed by your team;
• Writing detailed technical analysis documents.

THE SKILLS THAT WILL MAKE YOU AN ESSENTIAL MEMBER OF OUR TEAM
• You have completed at least two years of a bachelor''s degree in a relevant or related field (computer science, computer or software engineering, mathematics, etc.);
• You enjoy and are proficient in object-oriented programming;
• You enjoy working in a team and being in a collaborative environment;
• You communicate fluently in French, both spoken and written.

PRÊT.E À TRACER LA VOIE AVEC NOUS?

Postule dès maintenant et échange avec notre équipe d’acquisition de talents. Nous avons hâte de te rencontrer! Si possible, merci de nous faire parvenir ton CV en français.

Conformément aux exigences normatives et réglementaires auxquelles GIRO souscrit, tous les postes, qu''ils soient à durée indéterminée, à durée déterminée ou de stage, doivent faire l''objet d''une vérification d''antécédents judiciaires. Les postes dont l''exercice implique l''accès à des données financières doivent faire l''objet d''une enquête de crédit. Les vérifications sont réalisées selon les procédures en place chez GIRO.

Conditions d’emploi : Les candidats doivent être légalement autorisés à travailler dans le pays choisi au moment où un emploi leur est offert. Il incombe entièrement aux candidats posant leur candidature d’obtenir les permis de travail, les visas ou toutes autres autorisations nécessaires avant leur entrée en fonction.

Le générique masculin est utilisé uniquement dans le but d’alléger le texte.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:36:22.553145', true, 16);
INSERT INTO public.raw_postings VALUES (11, 'jsearch', 'https://simplify.jobs/p/48f1110d-0c11-4767-b26e-05b7d315526d/Software-Developer--4-months-InternshipCoop?utm_source=GHList&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Software Developer – 4 months Internship/Coop, Summer 2026
Company: Intact
Location: Montreal, Quebec CA
Employment Type: Internship
Posted: 2026-01-05T00:00:00.000Z

Salary: Not specified

Description:
Our employees are at the heart of everything we do. Together, we help people, businesses, and society prosper in good times and be resilient in bad times.

Our employee promise represents Intact’s commitment to you in exchange for living our Values, striving to do your best work, being open to change and investing in your career. In return, we promise to provide support, opportunities and performance-led financial rewards at a workplace where you can shape the future, win as a team and grow with us.

Salary for the candidate will be determined taking into consideration a number of factors including: experience, skills, qualifications, anticipated contribution to role, internal equity, etc. The salary range presented below is based on a 35-hour workweek and would represent a majority of different candidate profiles. However, we encourage candidates who may fall outside of this range to apply as well.

Salary range (but not limited to):
61,500 - 76,900

About the role

Launching your tech career at Intact means joining a diverse team of more than 3,000 Digital, Data and Tech experts working at the intersection of what exists and what’s possible. Here, you’ll be supported by forward-thinking leaders who celebrate shared success, and you’ll help push the industry forward with digital solutions that go beyond insurance to offer everyday value to millions of people. You’ll grow personally and professionally with access to cutting-edge technology-driven learning platforms and make lasting connections near and far. Most importantly, you’ll discover how exciting the “real world” can be.
Here, your career will take off 🚀

What you’ll do here :

Are you passionate about software development? Is your sweet spot at the forefront of digital innovation? Are you an advocate for great code and great design? We’ve got the perfect opportunity for you. We are seeking several talented Software Development Interns, specializing in back-end, front-end and full stack development, to join our dynamic and growing team!

Please note: This posting is hiring for student interns for multiple different teams in IT and Lab, for both Full Stack and Back End development. In the next step in the assessment process, you''ll be able to clarify which position type interests you best between IT/Lab/Full Stack or Back End***

In the Back-End Developer Intern role, you will :
• Work with the development team to coordinate the development of new features and resolve issues;
• Learn how to design, code, and test new features of our policy management system.
• Discover what it''s like to work as a Developer and how technological advances are changing the way insurance companies do business;
• Explore new ideas and learn best practices in a fun and inclusive environment;
• Technical skills required: Java/Kotlin, Docker/Kubernetes, AWS, RabbitMQ, Kafka, Spring Boot/Spring Cloud, Maven, Git and MongoDB/Oracle

In the Full-Stack Developer Intern role, you will:
• Participate in the development of Client Centre APIs in Java, Kotlin, and Nest;
• Adjust unit tests to ensure the quality of the new development;
• Adjust the technical documentation supporting the code;
• Technical skills required: Java/Kotlin, React, Spring/Spring Boot/Spring MVC, and microservices. For Front-End: Angular/React and typescript.

What you bring to the table: 
• Currently pursing a Bachelor''s, Master''s, or PhD degree in a field related to software development, computer science, or any other related field;
• Have at least one prior internship in a similar or related role;
• Understand the software development lifecycle and be curious about continuous delivery pipelines and testing;
• Experience in a financial services company (an asset);
• Strong analytical abilities and problem-solving skills;
• Adaptability, curiosity, and a commitment to continuous learning;
• Excellent communication skills with a passion for technology;
• Self-reliant with a strong sense of responsibility, a team player with a good sense of leadership;
• Available to work with us full-time, 35 hours per week, for the Summer Term from May 4 to August 21;
• Must be an active student during your internship and/or returning to school in next Fall 2026 following your internship;
• Be bilingual for all Quebec roles (English and French). Need to interact regularly with colleagues across the country. 

Your career starts here.  Apply today! 

We can’t wait to learn more about you. When you complete your application, remember to include your resume and University/College transcript. We hire co-ops every semester (Winter, Summer and Fall)! 

We’re accepting applications now through January 23, 2026. All submissions will be reviewed during this time, as well as after the posting closes. 
Il s''agit d''un nouveau rôle au sein de notre équipe en plein croissance | This role is a new member of our growing team.

We are an equal opportunity employer

At Intact, our Value of respect is founded on seeing diversity as a strength. We strive to create an accessible workplace where employees feel valued, included and encouraged to share their unique perspectives.

We encourage applications from individuals who are members of equity-deserving groups, including but not limited to women, Indigenous peoples, persons with disabilities, Black people, and members of the 2SLGBTQI+ community.

As part of Intact’s commitment to reconciliation, we acknowledge that we work, meet and travel across the land currently called Canada, originally inhabited by First Nations, Metis and Inuit people. This history extends through many centuries and continues to evolve today.

We have policies to ensure equal access and participation for people with disabilities, including providing workplace adjustments (accommodations). A copy of applicable policies is available on request.

If we can provide a specific adjustment to make the recruitment process more accessible for you, please let us know when we reach out about a job opportunity. We’ll work with you to meet your needs.

Learn more about our recruitment process and your candidate journey here.

Please note that Intact does not provide sponsorship or other support for immigration-related matters including but not limited to employer-specific closed work permits. Candidates must be eligible to work in Canada from the anticipated start date and throughout their employment and are solely responsible for maintaining their work eligibility.

If you are an employee of Intact or belairdirect, please apply for this role on Internal Career Site.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:36:22.68407', true, 17);
INSERT INTO public.raw_postings VALUES (12, 'jsearch', 'https://ca.talent.com/view?id=3b483afdf769&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Telecom IT Intern : Networking, Linux & Kubernetes
Company: Ericsson
Location: Montreal, Quebec CA
Employment Type: Full-time
Posted: 2026-01-10T23:00:00.000Z

Salary: Not specified

Description:
Un leader mondial des télécommunications basé à Montréal offre un stage de quatre mois en informatique. Les candidats doivent être inscrits à un programme de master ou licence en informatique ou dans un domaine technique pertinent. Le stage implique d''apprendre et d''expérimenter des solutions de télécommunications complexes en collaboration avec des mentors et des collègues. Une bonne connaissance des réseaux IP, des systèmes Unix et des compétences en scripting est requise. Ce poste ne propose pas de parrainage à l''immigration.

#J-18808-Ljbffr

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:36:22.835948', true, 18);
INSERT INTO public.raw_postings VALUES (13, 'jsearch', 'https://www.ziprecruiter.com/c/Intelcom/Job/Software-Development-Intern-GeoCoding/-in-Montreal,QC?jid=dd14fb4f7682d750&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Software Development Intern - GeoCoding
Company: Intelcom
Location: Montreal, Quebec CA
Employment Type: Full-time
Posted: 2025-12-29T00:00:00.000Z

Salary: Not specified

Description:
Make your internship count

At Intelcom, interns don''t just observe, they contribute meaningfully to real projects that shape how we operate. You''ll gain hands-on experience, grow your skills, and explore long-term career opportunities in a fast-moving, innovation-driven environment.

Ride the next mile with us!

We are seeking a Software Development Intern to support the implementation of Intelcom''s GeoCoding service. This is an exciting opportunity to apply your skills in a collaborative environment working on address coordination micro-services.

Responsibilities
• Participate in the development, testing, and maintenance of GeoCoding software services using Java.
• Collaborate to translate requirements into technical solutions.
• Write clean, efficient, and scalable code, along with comprehensive tests to ensure reliability and performance.
• Use CI/CD practices to build, test and deploy code changes.
• Participate in your team''s agile scrum sprints and ceremonies
• Participate in code reviews and provide constructive feedback.
• Contribute to troubleshooting, debugging, and optimizing the system.
• Support the deployment of software updates and maintenance of system performance.
• The role involves daily (or regular) communication with pan-Canadian stakeholders.

Qualifications
• Currently pursuing a bachelor''s in computer science, software engineering, or a related field.
• Proficient in Java.
• Knowledge of additional programming languages, including C#.
• Experience with AWS or Azure is an asset.
• Strong understanding of data structures.
• Experience designing and implementing relational databases
• Logical, analytical, and creative approach to problem-solving
• Strong collaboration and communication skills

#LI-DNI #IG-DNI

Intelcom is a leading last-mile carrier in the e-commerce sector. Our teams across Canada as well as our network of independent contractors contribute to Intelcom''s daily operations.

Our goal is simple: in a constantly evolving business sector, we don''t just follow, we get ahead. In addition to standing out through innovative services and delivery methods, Intelcom is also undergoing a technological transformation where the integration of customer experience and logistics technologies are at the heart of its evolution.

At Intelcom, we know experience comes in many forms and are committed to building a culture where difference is valued. We are always looking for talented and diverse individuals to join our teams. With over 60 delivery centers across Canada, we may have the right opportunity for you.

Apply Now.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:36:22.860453', true, 19);
INSERT INTO public.raw_postings VALUES (14, 'jsearch', 'https://jobs.bostonscientific.com/job/Montreal-Software-Development-Intern-Stagiaire-en-d%C3%A9veloppement-de-logiciels-QC/1351385800/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Software Development Intern / Stagiaire en développement de logiciels
Company: Boston Scientific
Location: Montreal, Quebec CA
Employment Type: Contractor and Internship
Posted: 2025-12-21T00:00:00.000Z

Salary: Not specified

Description:
Additional Location(s): Canada-QC-Montreal

Diversity - Innovation - Caring - Global Collaboration - Winning Spirit - High Performance

At Boston Scientific, we’ll give you the opportunity to harness all that’s within you by working in teams of diverse and high-performing employees, tackling some of the most important health industry challenges. With access to the latest tools, information and training, we’ll help you in advancing your skills and career. Here, you’ll be supported in progressing – whatever your ambitions.

Please note this is a 6-month contract opportunity beginning as soon as possible.

About the role

As a Software Development Intern, you''ll apply your technical skills to support the development and enhancement of software solutions. Working closely with our innovative engineering teams, you''ll contribute to coding, testing, and troubleshooting to improve system functionality. This role offers hands-on experience with key programming languages and the chance to collaborate on innovative projects, helping you grow your expertise in a fast-paced tech environment.

Your responsibilities will include:
• Writing regression test cases and performing functional testing for GUI development.
• Software tools development.
• Troubleshoot and diagnose issues with equipment and devices.
• Design Documentation.
• Other duties as required.

Required qualifications:
• Undergraduate or master''s degree (or working towards) in engineering or a related field
• 1+ years of relevant experience in software development (or equivalent combination of school and work experience)
• Proficiency in programming languages such as C++, Java, and Python
• Experience with XAML/QML and styling user controls for graphical user interfaces (GUIs)
• Solid understanding of design patterns, including MVC, MVVM, Singleton, Observer, and others
• Strong analytical skills with a demonstrated ability to troubleshoot and resolve complex issues
• Exceptional communication skills, fluent in both written and spoken English.

Preferred qualifications:
• Knowledge of Bluetooth, CanBus, USB, and I2C
• Working proficiency in French.

Veuillez noter qu’il s’agit d’une occasion de contrat d’une durée de six mois, débutant dès que possible

À propos du poste

En tant que stagiaire en développement de logiciels, vous mettrez vos compétences techniques au service du développement et de l’amélioration de solutions logicielles. En travaillant en étroite collaboration avec nos équipes d’ingénieurs innovantes, vous participerez au codage, aux essais et à la résolution des problèmes afin d’améliorer les fonctionnalités des systèmes. Vous acquerrez une expérience pratique dans les principaux langages de programmation et aurez la possibilité de collaborer à des projets novateurs, ce qui vous permettra d’approfondir votre expertise dans un environnement technologique en constante évolution.

Responsabilités :
• Rédaction des cas de test de régression et réalisation des tests fonctionnels pour le développement des interfaces graphiques (GUI).
• Concevoir des outils logiciels.
• Rechercher les pannes et diagnostiquer les problèmes liés aux équipements et aux appareils.
• Rédiger de la documentation.
• Autres tâches selon les besoins.

Compétences requises :
• Diplôme de premier cycle ou de maîtrise (ou en cours d’obtention) en ingénierie ou dans un domaine connexe
• Au moins une année d’expérience pertinente dans le développement de logiciels (ou combinaison équivalente d’études et d’expérience professionnelle)
• Maîtrise des langages de programmation tels que C++, Java et Python
• Expérience avec XAML/QML et les contrôles utilisateur de style pour les interfaces utilisateur graphiques (IUG).
• Solide compréhension des modèles de conception, notamment MVC, MVVM, Singleton, Observer, etc.
• Solides compétences analytiques et capacité avérée à résoudre des problèmes complexes.
• Compétences exceptionnelles en matière de communication, maîtrise de l’anglais à l’écrit et à l’oral.

Compétences souhaitées :
• Connaissance pratique de BlueTooth, CanBus, USB, I2C.
• Une bonne connaissance du français.

Requisition ID: 621117

Minimum Salary: $31200

Maximum Salary: $56800

The anticipated compensation listed above and the value of core and optional employee benefits offered by Boston Scientific (BSC) – see www.bscbenefitsconnect.com--will vary based on actual location of the position and other pertinent factors considered in determining actual compensation for the role. Compensation will be commensurate with demonstrable level of experience and training, pertinent education including licensure and certifications, among other relevant business or organizational needs. At BSC, it is not typical for an individual to be hired near the bottom or top of the anticipated salary range listed above.

Compensation for hourly, non-sales roles may also include variable compensation from time to time (e.g., any overtime and shift differential) and annual bonus target (subject to plan eligibility and other requirements).

Compensation for salaried, non-sales roles may also include variable compensation, i.e., annual bonus target and long-term incentives (subject to plan eligibility and other requirements).

Compensation for sales roles is governed by Sales Incentive Compensation Plan (which includes certain annual non-discretionary incentives based on predetermined objectives).

Our organization is across Canada and has commercial representation in 140 countries.

This job involves regular collaboration with colleagues, clients, and stakeholders across Canada, the U.S., and/or internationally, making proficiency in English essential for effective communication and alignment. English is necessary for engaging with a range of documentation and maintaining effective communication if interacting with external clients or vendors.

As detailed in the job description, this job involves communicating, both verbally and in writing, with other Boston Scientific teams located across Canada, the United States and/or with our international clients and partners. International customers and partners represent an important part of our activities. Based on an evaluation, we have determined that the duties of Software Development Intern / Stagiaire en développement de logicielsposition require knowledge of English in addition to French (oral and written). We also determined that the English language skills already required of other employees do not permit the performance of English language skills tasks related to Software Development Intern / Stagiaire en développement de logiciels position.

However, in Québec, Boston Scientific limits as much as possible the number of positions for which it requires the knowledge of another language than French. Boston Scientific solely requires proficiency in English where it is necessary for the performance of an employee’s duties.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:36:22.936074', true, 20);
INSERT INTO public.raw_postings VALUES (15, 'jsearch', 'https://ca.trabajo.org/job-3804-43d7e786588863fc10aeac9a5445776d?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Software Developer – 4 months Internship/Coop
Company: Intact
Location: Montreal, Quebec CA
Employment Type: Full-time
Posted: 2026-01-08T00:00:00.000Z

Salary: Not specified

Description:
Our employees are at the heart of everything we do. Together, we help people, businesses, and society prosper in good times and be resilient in bad times.

Our employee promise represents Intact''s commitment to you in exchange for living our Values, striving to do your best work, being open to change and investing in your career. In return, we promise to provide support, opportunities and performance-led financial rewards at a workplace where you can shape the future, win as a team and grow with us.

Salary for the candidate will be determined taking into consideration a number of factors including: experience, skills, qualifications, anticipated contribution to role, internal equity, etc. The salary range presented below is based on a 35-hour workweek and would represent a majority of different candidate profiles. However, we encourage candidates who may fall outside of this range to apply as well.

Salary range (but not limited to):

61, ,900

About the role

Launching your tech career at Intact means joining a diverse team of more than 3,000 Digital, Data and Tech experts working at the intersection of what exists and what''s possible. Here, you''ll be supported by forward-thinking leaders who celebrate shared success, and you''ll help push the industry forward with digital solutions that go beyond insurance to offer everyday value to millions of people. You''ll grow personally and professionally with access to cutting-edge technology-driven learning platforms and make lasting connections near and far. Most importantly, you''ll discover how exciting the "real world" can be.

Here, your career will take off

What you''ll do here :

Are you passionate about software development? Is your sweet spot at the forefront of digital innovation? Are you an advocate for great code and great design? We''ve got the perfect opportunity for you. We are seeking several talented Software Development Interns, specializing in back-end, front-end and full stack development, to join our dynamic and growing team

Please note: This posting is hiring for student interns for multiple different teams in IT and Lab, for both Full Stack and Back End development. In the next step in the assessment process, you''ll be able to clarify which position type interests you best between IT/Lab/Full Stack or Back End***

In the Back-End Developer Intern role, you will :
• Work with the development team to coordinate the development of new features and resolve issues;
• Learn how to design, code, and test new features of our policy management system.
• Discover what it''s like to work as a Developer and how technological advances are changing the way insurance companies do business;
• Explore new ideas and learn best practices in a fun and inclusive environment;
• Technical skills required: Java/Kotlin, Docker/Kubernetes, AWS, RabbitMQ, Kafka, Spring Boot/Spring Cloud, Maven, Git and MongoDB/Oracle

In the Full-Stack Developer Intern role, you will:
• Participate in the development of Client Centre APIs in Java, Kotlin, and Nest;
• Adjust unit tests to ensure the quality of the new development;
• Adjust the technical documentation supporting the code;
• Technical skills required: Java/Kotlin, React, Spring/Spring Boot/Spring MVC, and microservices. For Front-End: Angular/React and typescript.

What you bring to the table:
• Currently pursing a Bachelor''s, Master''s, or PhD degree in a field related to software development, computer science, or any other related field;
• Have at least one prior internship in a similar or related role;
• Understand the software development lifecycle and be curious about continuous delivery pipelines and testing;
• Experience in a financial services company (an asset);
• Strong analytical abilities and problem-solving skills;
• Adaptability, curiosity, and a commitment to continuous learning;
• Excellent communication skills with a passion for technology;
• Self-reliant with a strong sense of responsibility, a team player with a good sense of leadership;
• Available to work with us full-time, 35 hours per week, for the Summer Term from May 4 to August 21;
• Must be an active student during your internship and/or returning to school in next Fall 2026 following your internship;
• Be bilingual for all Quebec roles (English and French). Need to interact regularly with colleagues across the country.

Your career starts here. Apply today

We can''t wait to learn more about you. When you complete your application, remember to include your resume and University/College transcript. We hire co-ops every semester (Winter, Summer and Fall)

We''re accepting applications now through January 23, 2026. All submissions will be reviewed during this time, as well as after the posting closes.

Il s''agit d''un nouveau rôle au sein de notre équipe en plein croissance | This role is a new member of our growing team.

We are an equal opportunity employer

At Intact, our Value of respect is founded on seeing diversity as a strength. We strive to create an accessible workplace where employees feel valued, included and encouraged to share their unique perspectives.

We encourage applications from individuals who are members of equity-deserving groups, including but not limited to women, Indigenous peoples, persons with disabilities, Black people, and members of the 2SLGBTQI+ community.

As part of Intact''s commitment to reconciliation, we acknowledge that we work, meet and travel across the land currently called Canada, originally inhabited by First Nations, Metis and Inuit people. This history extends through many centuries and continues to evolve today.

We have policies to ensure equal access and participation for people with disabilities, including providing workplace adjustments (accommodations). A copy of applicable policies is available on request.

If we can provide a specific adjustment to make the recruitment process more accessible for you, please let us know when we reach out about a job opportunity. We''ll work with you to meet your needs.

Learn more about our recruitment process and your candidate journey here.

Please note that Intact does not provide sponsorship or other support for immigration-related matters including but not limited to employer-specific closed work permits. Candidates must be eligible to work in Canada from the anticipated start date and throughout their employment and are solely responsible for maintaining their work eligibility.

If you are an employee of Intact or belairdirect, please apply for this role on Internal Career Site.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:36:22.991604', true, 21);
INSERT INTO public.raw_postings VALUES (16, 'jsearch', 'https://www.learn4good.com/jobs/montreal/canada/info_technology/4773705551/e/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Summer Student RBC Borealis -Machine Learning Software Engineer Montreal
Company: 0000050007 Royal Bank of Canada
Location: Montreal, Quebec CA
Employment Type: Full-time, Contractor and Internship
Posted: 2026-01-09T00:00:00.000Z

Salary: Not specified

Description:
Position: 2026 Summer Student Opportunities RBC Borealis -Machine Learning Software Engineer, 4 Months - Montreal
Location: Montreal

Job Description
LOCATION: Montreal
What’s the opportunity?We’re looking for an enthusiastic software engineer who’s excited by the opportunity of being at the forefront of machine learning technology, and working on extremely challenging problems. As a Co-op Machine Learning Software Engineer
, you’ll be involved a project end to end – everything from data pre-processing to implementing machine learning algorithms and front-end development.

At RBC Borealis, you’ll be joining a team that works directly with leading researchers in machine learning, has access to rich and massive datasets, and offers the computational resources to support ongoing development in areas such as reinforcement learning, unsupervised learning and computer vision. You can find out more about our research areas at Your responsibilities include:
• Building machine learning-based software solutions for solving important problems;
• Collaborating with research and business teams to converge on the best solutions;
• Optimizing algorithms and prototypical solutions for efficient implementation;
• Extending prototypes into fully functional, polished solutions ready for internal and/or external use;
• Supporting projects with thorough documentation of usage, design decisions and capabilities;
• Extracting, transforming and loading massive datasets using distributed computing framework technologies (Hadoop, Spark, etc.);
You’re our ideal candidate if you:
• Are working on a bachelors or masters degree in Computer Science, Computer Engineering, Software Engineering, or equivalent;
• Have some software development experience (including co-op and internships);
• Have experience with writing software in one of the major languages such as C++, C#, Java, Python;
• Have familiarity with the Unix command line and bash scripting;
• Experience with Deep Learning packages such as Tensorflow, Theano, Keras and PyTorch is an asset;
• Exposure to distributed computing frameworks (e.g. Hadoop, Spark) as well as SQL, No

SQL and graph databases is an asset;
What''s in it for you?
• Become part of a team that thinks progressively and works collaboratively. We care about seeing each other reach full potential;
• Ability to make a difference and lasting impact from a local-to-global scale.
About RBC Borealis
RBC Borealis is the driving force behind Royal Bank of Canada’s AI and data innovation. As part of Canada’s largest financial institution, we bring together a team of architects, engineers, scientists, and product experts on a mission to revolutionize finance through world-class research, solutions, and a resilient data platform. With locations across Toronto, Waterloo, Montreal, Calgary, and Vancouver, we’re at the forefront of AI research and platform development.

With a focus on cutting-edge research in areas like time series forecasting, causal machine learning, and responsible AI, we are seamlessly integrating AI research and data engineering, to solve critical challenges in the financial industry. We are building intelligent, and scalable, data-driven solutions that will help communities thrive and drive innovation for our customers across the bank.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:36:23.089465', true, 22);
INSERT INTO public.raw_postings VALUES (17, 'jsearch', 'https://www.ziprecruiter.com/c/Intelcom/Job/Software-Development-Intern-Mobile-Application/-in-Montreal,QC?jid=9eb4b37c1d43d777&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Software Development Intern - Mobile Application
Company: Intelcom
Location: Montreal, Quebec CA
Employment Type: Full-time
Posted: 2025-12-29T00:00:00.000Z

Salary: Not specified

Description:
Make your internship count

At Intelcom, interns don''t just observe, they contribute meaningfully to real projects that shape how we operate. You''ll gain hands-on experience, grow your skills, and explore long-term career opportunities in a fast-moving, innovation-driven environment.

Ride the next mile with us!

We are seeking a Software Development Intern to join our Mobile Application team to enhance driver experience. This is an exciting opportunity to gain hands-on experience in building and enhancing mobile system functionality and efficiency.

Responsibilities
• Participate in the development, testing and maintenance of the Route Application using MAUI.net (C#)
• Collaborate with the operations department to translate requirements into technical solutions aligned with driver''s needs and operational workflows
• Build proofs of concepts (POCs) for mobile application
• Write clean, efficient and scalable code
• Participate in code reviews and provide constructive feedback
• Contribute to troubleshooting, debugging and optimizing mobile application features
• Support the deployment of mobile app updates and ensure performance reliability
• The role involves daily (or regular) communication with pan-Canadian stakeholders.

Qualifications
• Currently pursuing a bachelor''s degree in Computer Science, Software Engineering, or a related field.
• Proficient in C#.
• Knowledge of additional programming languages, including Java, Python and JavaScript, an asset.
• Knowledge of web development frameworks and databases is an asset.
• Logical, analytical, and creative approach to problem-solving
• Strong collaboration and communication skills with an eagerness to learn

#LI-DNI #IG-DNI

Intelcom is a leading last-mile carrier in the e-commerce sector. Our teams across Canada as well as our network of independent contractors contribute to Intelcom''s daily operations.

Our goal is simple: in a constantly evolving business sector, we don''t just follow, we get ahead. In addition to standing out through innovative services and delivery methods, Intelcom is also undergoing a technological transformation where the integration of customer experience and logistics technologies are at the heart of its evolution.

At Intelcom, we know experience comes in many forms and are committed to building a culture where difference is valued. We are always looking for talented and diverse individuals to join our teams. With over 60 delivery centers across Canada, we may have the right opportunity for you.

Apply Now.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:36:23.176214', true, 23);
INSERT INTO public.raw_postings VALUES (18, 'jsearch', 'https://www.recruit.net/job/software-engineer-full-stack-react-jobs/BC1179902FDAB9E3?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Junior Software Engineer (Full Stack, React and Node)
Company: CSC Generation
Location: Montreal, Quebec CA
Employment Type: Internship
Posted: 2026-01-09T00:00:00.000Z

Salary: Not specified

Description:
CSC Generation is a technology driven holding company that acquires and operates established consumer brands, including One Kings Lane, Backcountry, and Sur La Table. Across 13 brands generating over $1B in annual revenue, we improve how these businesses run by building shared platforms, automation, and data tooling that scale across the portfolio.

This role is platform work at the intersection of e-commerce, operations, and data. You will ship production changes used daily, and you will learn reliable delivery through small pull requests, code review, and disciplined debugging.

This Junior Software Engineer role is for early career full-stack engineers who want to grow quickly. You will work primarily in JavaScript and TypeScript, with React on the front end and Node on the back end, and over time you will own small features end to end.

What you get to do:
• Build and refine user facing features using React, TypeScript, and modernfront endtooling.
• Implement and integrate simple backend services using Node and TypeScript or JavaScript, including REST style APIs and basic data models.
• Work with senior engineers to break down requirements into small, shippable pieces and implement them end to end.
• Write clear, maintainable code and basic tests for both front end andback endfunctionality.
• Collaborate with product and design to polish UX details, handle edge cases, and improve performance and reliability.
• Use AIassistedtools, such as ChatGPT or GitHub Copilot, in a disciplined way to speed up development while keeping code quality high.
• Participatein code reviews, ask questions, and steadily grow toward owning small features and services independently.
• Practice good engineering hygiene: version control, small pull requests, clear commit messages, and lightweight documentation.
• Invest in your own growth: read documentation, keep notes, and reflect on feedback you receive.

What you bring:
• You do not need to check every box. We are open to candidates who are early in their careers but show strong fundamentals and learning habits.
• Experience with JavaScript or TypeScript through coursework, internships, personal projects, bootcamps, or 0 to 3 years of professional work.
• Somehands-onexperience with React andcomponent basedUI development, including state management and basic forms.
• Some exposure to backend development in Node, for example simple APIs, scripts, orserver sidelogic.
• Comfort with HTML and CSS, responsive layouts, and common web patterns.
• Basic understanding of HTTP, JSON, and howfront endcode communicates with backend services.
• Some exposure to testing tools on either front end or back end, or a clear willingness to learn them.
• Strong debugging mindset: you read error messages, check logs, and try small experiments before asking for help.
• Evidence of being studious andself directed. For example:
• Youmaintainpersonal notes or a knowledge base.
• You can describe something difficult you taught yourself recently and how you went about it.
• Clear communication, willingness to receive feedback, and a growth mindset.

Nice to have
• Experience with a web framework such as Express, Next.js, or similar.
• Exposure to databases or data storage, even if only in simple projects.
• Awareness of accessibility, performance, and basic security considerations.
• Prior use of AI coding assistants or strong interest in using them responsibly in your workflow.
• Experience with ecommerce, design systems, orcomponentlibraries.

How we hire for this role:
• We use two small, focused exercises as part of the process:
• A front end React and TypeScript exercise that looks like a real feature you might ship.
• A simple backend Node exercise that tests API and data modeling fundamentals.

We look for:
• Clear, readable code and correct behavior for the core requirements.
• A methodical approach to state and data, not clever tricks.
• Evidence that you read the specification carefully and handle edge cases thoughtfully.
• Perfect completion is notrequired. We care a lot about:
• Howyouapproach problems when you areuncertain.
• Whether you leave comments ornoteswhen you run out of time.
• How you explain your decisions and describe what you would improve with more time.
• Later stages focus on how you debug in real time, how you respond to feedback, and how you work with frustration and ambiguity without shutting down.

What''s in it for you:
• This role is designed to turn early career engineers into reliable full stack contributors through real production work and tight feedback loops. You will ship user-facing features, contribute to backend services, and learn the day to day engineering habits that matter most: scoping work into small increments, writing readable code, reviewing code thoughtfully, and debugging issues end to end.
• Within your first 6 months, you will ship production changes and take ownership of clearly scoped features with light guidance through code review. Diligent engineers in this role often move faster, owning larger features earlier than is typical for junior roles, because we favor small teams, fast iteration, and real responsibility. The pace is real, and support is there when you need it, but you are expected to drive.

In addition to competitive compensation, we offer:
• Executive Access: Direct access to decision makers so good ideas do not get stuck in long approval chains, and so your work can ship faster.
• AI-First Skill Building: Hands on experience using AI-assisted development tools with the same expectations we have for any code: reviewable, testable, and maintainable.
• Career Growth: Increasing scope and ownership based on demonstrated readiness, including opportunities to expand across frontend and backend work as you develop.
• Competitive benefits: Paid time off policies, 401(k)/RRSP match, medical, dental, vision, supplemental policies, and employee discounts at our portfolio companies.

The CSC family of brands provides equal employment opportunities to all employees and applicants for employment and prohibits discrimination and harassment of any type without regard to race, color, religion, age, sex, national origin, disability status, genetics, protected veteran status, sexual orientation, gender identity or expression, or any other characteristic protected by federal, provincial, state or local laws.

The CSC family of brands is committed to providing reasonable accommodations for qualified individuals with disabilities in our job application procedures. If you need assistance or an accommodation due to a disability, please contact

#J-18808-Ljbffr

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:36:23.225549', true, 24);
INSERT INTO public.raw_postings VALUES (19, 'jsearch', 'https://www.recruit.net/job/software-developer-cloud-g-microservices-jobs/6C1D1EB86A0D1315?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Software Developer Intern – Cloud & 5G Microservices (Montreal)
Company: Ericsson GmbH
Location: Montreal, Quebec CA
Employment Type: Internship
Posted: 2026-01-10T23:00:00.000Z

Salary: Not specified

Description:
Une entreprise technologique internationale basée à Montréal recherche un stagiaire développeur de logiciels pour rejoindre une équipe innovante. Vous serez impliqué dans l''amélioration du cadre de surveillance des tests et contribuerez à la création de tests automatisés. Les candidats doivent avoir des connaissances en Java et JavaScript ainsi que de bonnes compétences en communication. Ce stage est une excellente opportunité pour les étudiants en ingénierie ou en informatique.
#J-18808-Ljbffr

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:41:41.248597', true, 25);
INSERT INTO public.raw_postings VALUES (20, 'jsearch', 'https://en-ca.whatjobs.com/jobs/apprentice-software-developer?id=100962469&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Apprentice Software Developer
Company: WhatJobs Direct
Location: Montreal, Quebec CA
Employment Type: Internship
Posted: 2026-01-08T00:00:00.000Z

Salary: Not specified

Description:
Our client is excited to offer a unique Apprenticeship program for aspiring Software Developers. This is a fully remote, immersive learning experience designed to equip individuals with the foundational skills and practical knowledge needed to excel in the tech industry. You will be paired with experienced mentors who will guide you through coding best practices, software development lifecycle, and various programming languages. This role is perfect for individuals with a passion for technology, a strong aptitude for problem-solving, and a desire to build a career in software development, all from the comfort of your home office. As a remote-first program, we leverage cutting-edge collaboration tools to ensure a connected and productive environment.

Program Highlights: Hands-on training in modern programming languages (e.g., Python, JavaScript, Java). Exposure to full-stack development, including front-end and back-end technologies. Learning industry-standard development tools and methodologies (e.g., Git, Agile). Development of critical thinking and problem-solving skills through real-world projects. Mentorship from senior software engineers. Opportunity to contribute to impactful software solutions. Gain valuable experience and build a professional network. Ideal Candidate Profile: A demonstrable passion for software development and technology. Basic understanding of programming concepts is beneficial but not strictly required. Excellent communication and interpersonal skills, essential for remote collaboration. Strong motivation to learn and grow within a fast-paced environment. Ability to work independently and manage time effectively in a remote setting. Completion of a secondary education program or equivalent experience. Eagerness to embrace new challenges and contribute to team success. This apprenticeship offers a gateway into a rewarding career in software development, providing comprehensive training and practical experience in a supportive, remote setting. If you are eager to learn and build your future in technology, apply today to be considered for this exciting opportunity in **Montreal, Quebec, CA**.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:41:41.317188', true, 26);
INSERT INTO public.raw_postings VALUES (21, 'jsearch', 'https://www.recruit.net/job/co-op-developer-tools-engineer-jobs/9172EB1D98A22F87?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Co-op: Developer Tools Engineer
Company: Safety CLI
Location: Montreal, Quebec CA
Employment Type: Full-time
Posted: 2026-01-09T00:00:00.000Z

Salary: Not specified

Description:
Safety Cybersecurity is dedicated to helping development teams build and deploy secure applications with confidence. Our cutting-edge platform integrates seamlessly into the development workflow, providing real-time vulnerability detection and actionable remediation guidance. We are focused on building the world’s first AI-powered software supply chain firewall.

The Opportunity

We''re looking for a motivated Computer Science student, including those participating in the Venture For Canada summer intern program, to join our Product team for a co-op position. As a Developer Tools Engineer intern, you''ll have the exciting opportunity to work on extending our platform''s capabilities to support various Integrated Development Environments (IDEs). This role offers hands-on experience in a fast-paced cybersecurity environment where you''ll contribute directly to our product''s evolution.

What You’ll Do
• Design and implement IDE extensions that integrate the Safety platform into developers’ preferred environments
• Collaborate with our product and engineering teams to understand user needs and technical requirements
• Write clean, maintainable Python code with proper documentation and tests
• Participate in code reviews and technical discussions
• Learn about cybersecurity best practices and how they apply to development workflows
• Present your work and findings to the broader team

Qualifications
• Currently enrolled in a Computer Science or related program at a Canadian university or college
• Experience with Python programming
• Basic understanding of software development processes and tools
• Familiarity with version control systems (Git)
• Interest in cybersecurity and developer tools
• Strong problem‑solving abilities and attention to detail

Nice to Have
• Previous experience with IDE extension development
• Familiarity with REST APIs
• Understanding of security concepts and common vulnerabilities
• Experience with CI/CD pipelines

What We Offer
• Mentorship from experienced engineers
• Opportunity to work on a meaningful project with real‑world impact
• Collaborative and inclusive team environment
• Learning and development opportunities
• Fun team events and activities

Location
• Remote across Canada, but possibility to work from our office in Vancouver

How to Apply

Please submit your resume, cover letter, and any relevant portfolio links or GitHub projects. In your cover letter, please share why you’re interested in developer tools and what excites you about improving the security of software development.

Safety Cybersecurity is an equal opportunity employer. We celebrate diversity and are committed to creating an inclusive environment for all employees.

Stay informed on emerging threats, novel attack vectors, and vulnerability research from Safety’s cybersecurity team. Technical analysis, not product updates.

#J-18808-Ljbffr

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:41:41.37042', true, 27);
INSERT INTO public.raw_postings VALUES (22, 'jsearch', 'https://ca.linkedin.com/jobs/view/intern-screen-content-tools-for-video-compression-coding-at-interdigital-inc-4315880139?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Intern, Screen Content tools for Video Compression/Coding
Company: InterDigital, Inc.
Location: Montreal, Quebec CA
Employment Type: Internship
Posted: 2026-01-10T00:00:00.000Z

Salary: Not specified

Description:
About InterDigital

InterDigital is a global research and development company focused primarily on wireless, video, artificial intelligence (“AI”), and related technologies. We design and develop foundational technologies that enable connected, immersive experiences in a broad range of communications and entertainment products and services. We license our innovations worldwide to companies providing such products and services, including makers of wireless communications devices, consumer electronics, IoT devices, cars and other motor vehicles, and providers of cloud-based services such as video streaming. As a leader in wireless technology, our engineers have designed and developed a wide range of innovations that are used in wireless products and networks, from the earliest digital cellular systems to 5G and today’s most advanced Wi-Fi technologies. We are also a leader in video processing and video encoding/decoding technology, with a significant AI research effort that intersects with both wireless and video technologies. Founded in 1972, InterDigital is listed on Nasdaq.

InterDigital is a registered trademark of InterDigital, Inc.

For more information, visit: www.interdigital.com.

About Your Video Lab Internship

State-of-the-art video codecs use a very diverse range of coding tools on different parts of the video codec, such as filtering, intra or inter coding, transforms, entropy coding, as well as for different scenarios, such as natural video content, screen content, gaming content, etc. Also, the use of some tools created for screen content videos has proven to be effective on natural content videos.

This internship is carried out in the R&I video coding team in Montreal. The student will get familiar with the state-of-the-art video codecs, will understand how screen content tools are used for video coding improvement. The student will analyze various of these tools that exist and work towards applying improved methods to the current and future video coding standards. The work will involve coding in C++ and a good background in digital signal processing is a must.

Roles & Responsibilities:
• Familiarize yourself with existing video coding standards such as HEVC and VVC.
• Work with reference model software (e.g., VTM, ECM) to understand current implementations.
• Review academic and industry literature on screen content coding tools.
• Enhance tool usage to improve video coding performance.
• Implement and test improved algorithms within the test model software.

Qualifications:
• Strong foundation in digital signal processing.
• Proficient in C++ programming.
• Knowledge of video coding is preferred but not required.
• Experience with Python and shell scripting is a plus.

Keywords: MPEG, HEVC, VVC, Video Coding, Digital Signal Processing, C++

Expected Outcomes:
• Develop a clear understanding and documentation of screen content tools used in video codecs.
• Implement enhancements to existing tools in C++ within the test model software.
• Evaluate the performance of the improved tools and compare results with state-of-the-art methods.
• Produce a comprehensive report detailing the work completed during the internship.
• Deliver a final presentation to the R&I team summarizing findings and contributions.

This internship is available in 2026, please indicate your availability for a 4+ month internship in the questions associated with your application or a cover letter. Flexibility with start date.

Location: Montreal, Canada

InterDigital is an equal employment opportunity employer. InterDigital will not engage in or tolerate unlawful discrimination with regard to any employment decision, policy or practice based on a person’s sex, gender, pregnancy (including childbirth, breastfeeding and related medical conditions), age, race, color, religion, creed, national origin, ancestry, citizenship, military status, veteran status, mental or physical disability, medical condition, genetic information, sexual orientation, gender identity or expression, or any other factor protected by applicable federal, state or local law. This policy applies to all terms and conditions of employment, including, but not limited to, recruiting, hiring, compensation, benefits, training, assignments, evaluations, coaching, promotion, discipline, discharge and layoff.

______________________________________________________________________________

À propos d''InterDigital

InterDigital est une entreprise mondiale de recherche et de développement qui se concentre principalement sur les technologies sans fil, vidéo, d''intelligence artificielle ("AI") et les autres technologies connexes. Nous concevons et développons des technologies fondamentales qui permettent des expériences connectées et immersives dans une large gamme de produits et de services de communication et de divertissement. Nous concédons des licences sur nos innovations dans le monde entier à des entreprises qui fournissent de tels produits et services, notamment des fabricants d''appareils de communication sans fil, d''appareils électroniques grand public, d''appareils IoT, de voitures et d''autres véhicules à moteur, ainsi que des fournisseurs de services basés sur le cloud, tels que la diffusion vidéo. En tant que leader de la technologie sans fil, nos ingénieurs ont conçu et développé un large éventail d''innovations utilisées dans les produits et les réseaux sans fil, depuis les premiers systèmes cellulaires numériques jusqu''à la technologie 5G et les technologies Wi-Fi les plus avancées d''aujourd''hui. Nous sommes également un leader dans le domaine du traitement vidéo et de la technologie de codage/décodage vidéo, avec un important effort de recherche en matière d''IA qui recoupe à la fois les technologies sans fil et les technologies vidéo. Fondée en 1972, InterDigital est une société cotée au NASDAQ.

InterDigital est une marque déposée d''InterDigital, Inc.

Pour plus d''informations, n''hésitez pas à consulter le site www.interdigital.com.

Résumé

Les codecs vidéo à l’état de l’art reposent largement sur le codage par transformation, un outil essentiel pour représenter efficacement les signaux vidéo. Les recherches récentes en matière de codage vidéo ont introduit des transformations apprises et non séparables, offrant un potentiel considérable pour de nouveaux gains en compression. Ce stage sera effectué au sein de l’équipe R&I en codage vidéo à Montréal et portera sur la familiarisation avec ces nouvelles transformations, l’analyse de leur comportement et l’exploration de stratégies visant à améliorer leur efficacité. Le travail pourra inclure la conception d’approches adaptatives au contenu, l’affinement des méthodologies d’apprentissage et l’évaluation comparative des performances par rapport aux standards de codage existants tels que HEVC et VVC. L’étudiant·e acquerra une expérience pratique du développement en Python et en C++ dans le cadre d’une plateforme de codage vidéo de pointe, tout en développant une solide expertise en traitement du signal numérique et en techniques de codage par transformation.

Responsabilités

Les rôles et les responsabilités sont les suivants :
• examiner la littérature sur le codage par transformation,
• se familiariser avec les normes de codage vidéo existantes (telles que HEVC, VVC),
• améliorer les algorithmes d''apprentissage de transformation,
• tester les transformations améliorées dans le logiciel du modèle de test à l''aide des scripts fournis par l''équipe.

Qualifications
• Compétences en traitement numérique du signal
• Maîtrise des langages de programmation Python et C++
• La connaissance du codage vidéo est préférable mais pas obligatoire

Mots Clés :

Codage vidéo, HEVC, VVC, traitement numérique du signal, C++, Python

Résultats Attendus :
• Produire des ensembles de données et effectuer des transformations à l''aide des scripts fournis par l''équipe.
• Amélioration des scripts et intégration des nouvelles transformations dans le code C++ du logiciel de référence.
• Obtenir des résultats et comparer les différentes approches étudiées.
• Produire un rapport sur le travail effectué pendant le stage
• Faire une présentation de fin de stage à l''ensemble de l''équipe de recherche et d''innovation

Lieu : Montréal, Canada

InterDigital est un employeur offrant l''égalité des chances en matière d''emploi. InterDigital s''interdit de toute discrimination illégale et ne tolère aucune décision, politique ou pratique prise en matière d''emploi basée sur le sexe, le genre, la grossesse (y compris l''accouchement, l''allaitement et l''état de santé), l''âge, la race, la couleur, la religion, la croyance, l''origine nationale, l''ascendance, la citoyenneté, le statut militaire, le statut de vétéran, le handicap mental ou physique, l''état de santé, les informations génétiques, l''orientation sexuelle, l''identité ou l''expression de genre, ou tout autre facteur protégé par la loi fédérale, nationale ou locale applicable. Cette politique s''applique à toutes les conditions d''emploi, y compris, de façon non limitative, au recrutement, à l''embauche, à la rémunération, aux avantages sociaux, à la formation, aux affectations, aux évaluations, au coaching, à la promotion, à la discipline, au licenciement et à la mise à pied.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:41:41.419263', true, 28);
INSERT INTO public.raw_postings VALUES (23, 'jsearch', 'https://en-ca.whatjobs.com/jobs/developer?id=100960067&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Junior Software Developer - Apprenticeship Program, Remote
Company: WhatJobs Direct
Location: Montreal, Quebec CA
Employment Type: Internship
Posted: 2026-01-08T00:00:00.000Z

Salary: Not specified

Description:
Our client, a dynamic and rapidly expanding software development company, is excited to offer a unique Junior Software Developer opportunity through their fully remote Apprenticeship Program. This is an ideal entry-level position for aspiring developers eager to launch their careers in the tech industry. As an apprentice, you will receive hands-on training and mentorship from experienced engineers, working on real-world projects and gaining invaluable practical experience. You will learn to write, test, and debug code, collaborate with team members on software design and architecture, and contribute to the development of innovative applications. The curriculum is designed to provide a comprehensive understanding of software development principles, programming languages (e.g., Python, Java, JavaScript), and modern development tools and practices. This fully remote program allows you to learn and grow from the comfort of your home office, eliminating the need for relocation or daily commutes. We are seeking enthusiastic, motivated individuals with a passion for technology and a strong aptitude for problem-solving. While prior professional development experience is not required, a foundational understanding of programming concepts or completion of relevant online courses is beneficial. This apprenticeship is a fantastic pathway to a successful career in software engineering, providing structured learning, practical application, and the potential for full-time employment upon successful completion. This program is specifically designed for individuals looking to build a career in software development, based within the Montreal, Quebec, CA ecosystem but accessible remotely. Successful completion of the apprenticeship will equip you with in-demand skills and a strong portfolio. We encourage applications from individuals with a keen interest in coding, logical thinking, and continuous learning.

Program Details: Comprehensive training in modern software development languages and technologies. Hands-on project experience with mentorship from senior engineers. Development of skills in coding, testing, debugging, and software maintenance. Exposure to Agile development methodologies and collaborative team practices. Opportunity to contribute to impactful software projects. Structured learning path designed for career entry into the tech industry. Fully remote program offering flexibility and accessibility. Potential for full-time employment post-apprenticeship based on performance. Ideal Candidate Profile: High school diploma or equivalent; Bachelor''s degree in Computer Science or related field is a plus. Demonstrated passion for software development and technology. Basic understanding of programming logic and concepts is preferred. Strong analytical and problem-solving abilities. Excellent communication and teamwork skills. Self-motivated, eager to learn, and adaptable to new technologies. Ability to work independently and manage time effectively in a remote setting. Must be eligible to work in Canada.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:41:41.490811', true, 29);
INSERT INTO public.raw_postings VALUES (24, 'jsearch', 'https://en-ca.whatjobs.com/jobs/deep-learning?id=100928505&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Graduate Software Developer (AI Focus)
Company: WhatJobs Direct
Location: Montreal, Quebec CA
Employment Type: Internship
Posted: 2026-01-08T00:00:00.000Z

Salary: Not specified

Description:
Our client is offering an exciting Graduate Software Developer internship opportunity with a focus on Artificial Intelligence and Machine Learning. This is a fully remote role, allowing aspiring tech professionals to gain invaluable industry experience from anywhere in Canada. You will work alongside seasoned engineers on cutting-edge AI projects, contributing to the development of intelligent systems and algorithms. This internship is designed for motivated individuals seeking to launch their career in a challenging and rewarding environment, applying theoretical knowledge to real-world problems.

Responsibilities:
Assist in the design, development, and implementation of AI/ML models and algorithms. Write clean, efficient, and well-documented code in languages such as Python, Java, or C++. Collaborate with senior developers and researchers on AI research projects. Collect, clean, and preprocess data for training machine learning models. Participate in code reviews and contribute to improving code quality. Test and debug software components to ensure functionality and performance. Research and evaluate new AI technologies and tools. Contribute to the documentation of AI models and project progress. Attend team meetings and provide updates on assigned tasks. Learn and apply software development best practices and agile methodologies. Assist in the deployment and monitoring of AI applications. Develop a strong understanding of the company''s products and services through practical application. Engage in continuous learning to stay updated with the rapidly evolving field of AI.
Qualifications:
Currently pursuing or recently completed a Bachelor''s or Master''s degree in Computer Science, Artificial Intelligence, Data Science, or a related field. Foundational knowledge of AI/ML concepts, algorithms, and libraries (e.g., TensorFlow, PyTorch, scikit-learn). Proficiency in at least one programming language relevant to AI (e.g., Python). Familiarity with data structures and algorithms. Strong analytical and problem-solving skills. Excellent communication and teamwork abilities. Ability to work independently and manage time effectively in a remote setting. Eagerness to learn and adapt to new technologies. Previous project experience in AI/ML (academic or personal) is a plus. This internship provides a fantastic entry point into the AI sector, working on innovative projects based in Montreal, Quebec, CA , but conducted entirely remotely.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:41:41.54307', true, 30);
INSERT INTO public.raw_postings VALUES (25, 'jsearch', 'https://ca.linkedin.com/jobs/view/internship-it-sector-summer-2026-at-desjardins-4351795810?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Internship, IT sector, Summer 2026
Company: Desjardins
Location: Montreal West, Quebec CA
Employment Type: Full-time
Posted: 2026-01-07T00:00:00.000Z

Salary: Not specified

Description:
💚 Are You Looking For a One-of-kind Experience With An Outstanding Team In a Modern Environment? We’re Looking For Bright Interns Who Like To Learn Because With Our Squads, There’s Always Something New. Starting Your Career At Quebec’s Largest Private IT Employer, (we Have More Than 9,000 IT Employees!) Is An Opportunity Not To Be Missed. Desjardins Is a Top Employer That’s Committed To The Next Generation Of IT Professionals. There Are Several Internship Positions Available. More Specifically, We’re Looking For

📊Business administration intern
• Analyze issues related to your line of work, conduct research and preliminary analysis, develop initial outlines for tools and working processes, and draw on your comprehensive knowledge of the business segment while acting as an advisor to our dedicated clients and partners.

📐Operations systems analysis intern
• Implement the infrastructure in accordance with architectural specifications and operating standards, while contributing to the reliability, performance and compliance of IT environments.

🔍Quality assurance intern
• Actively participate in quality assurance tests, identifying test scenarios (unit, functional, system, non-regression), implementing the environment, carrying out scenarios and communicating results.

🚀Project management intern
• Support all stages of project delivery, from the planning stages all the way to the end result, while handling coordination duties, respecting deadlines and approving deliverables to ensure objectives are met.

💻Development intern
• Actively participate in the elaboration of a production strategy. Contribute to app and program analysis, design, coding, testing and documentation to ensure high-performance solutions that are adapted to specific needs.

🛡️ IT governance and compliance intern
• Participate in the development of IT governance and compliance approaches, document multiple internal processes and procedures related to risk and compliance practices, ensure the quality of evidence related to general IT controls, and follow up with compliance officers while monitoring certain files.

🧩Scrum master intern
• Support the team with sprint planning and assessments. Foster collaboration, eliminate obstacles and ensure Scrum best practices are followed to ensure optimal value at the time of delivery.

⭐ What You Bring To The Table
• Your educational institution must credit or certify your internship toward a bachelor’s degree or a master’s degree in an appropriate discipline.
• Relevant work/internship experience
• Knowledge of French required

At Desjardins, we don’t just support youth. We value their talent. There’s a difference.

Action oriented, Customer Focus, Differences, Nimble learning

At Desjardins, we believe in equity, diversity and inclusion. We''re committed to welcoming, respecting and valuing people for who they are as individuals, learning from their differences, embracing their uniqueness, and providing a positive workplace for all. At Desjardins, we have zero tolerance for discrimination of any kind. We believe our teams should reflect the diversity of the members, clients and communities we serve.

If there''s something we can do to help make the recruitment process or the job you''re applying for more accessible, let us know. We can provide accommodations at any stage in the recruitment process. Just ask!

Job Family

Information technology (FG)

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:50:56.241788', true, 31);
INSERT INTO public.raw_postings VALUES (26, 'jsearch', 'https://ca.indeed.com/viewjob?jk=9bfcf770aef1c3b6&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Internship, IT sector, Summer 2026
Company: Desjardins
Location: Montreal, Quebec CA
Employment Type: Full-time
Posted: 2026-01-07T00:00:00.000Z

Salary: Not specified

Description:
Are you looking for a one-of-kind experience with an outstanding team in a modern environment? We’re looking for bright interns who like to learn because with our squads, there’s always something new. Starting your career at Quebec’s largest private IT employer, (we have more than 9,000 IT employees!) is an opportunity not to be missed. Desjardins is a top employer that’s committed to the next generation of IT professionals. There are several internship positions available. More specifically, we’re looking for:

Business administration intern
• Analyze issues related to your line of work, conduct research and preliminary analysis, develop initial outlines for tools and working processes, and draw on your comprehensive knowledge of the business segment while acting as an advisor to our dedicated clients and partners.

Operations systems analysis intern
• Implement the infrastructure in accordance with architectural specifications and operating standards, while contributing to the reliability, performance and compliance of IT environments.

Quality assurance intern
• Actively participate in quality assurance tests, identifying test scenarios (unit, functional, system, non-regression), implementing the environment, carrying out scenarios and communicating results.

Project management intern
• Support all stages of project delivery, from the planning stages all the way to the end result, while handling coordination duties, respecting deadlines and approving deliverables to ensure objectives are met.

Development intern
• Actively participate in the elaboration of a production strategy. Contribute to app and program analysis, design, coding, testing and documentation to ensure high-performance solutions that are adapted to specific needs.

️ IT governance and compliance intern
• Participate in the development of IT governance and compliance approaches, document multiple internal processes and procedures related to risk and compliance practices, ensure the quality of evidence related to general IT controls, and follow up with compliance officers while monitoring certain files.

Scrum master intern
• Support the team with sprint planning and assessments. Foster collaboration, eliminate obstacles and ensure Scrum best practices are followed to ensure optimal value at the time of delivery.
• What you bring to the table
• Your educational institution must credit or certify your internship toward a bachelor’s degree or a master’s degree in an appropriate discipline.
• Relevant work/internship experience
• Knowledge of French required

At Desjardins, we don’t just support youth. We value their talent. There’s a difference.

#LI-Hybrid
Action oriented, Customer Focus, Differences, Nimble learning

At Desjardins, we believe in equity, diversity and inclusion. We''re committed to welcoming, respecting and valuing people for who they are as individuals, learning from their differences, embracing their uniqueness, and providing a positive workplace for all. At Desjardins, we have zero tolerance for discrimination of any kind. We believe our teams should reflect the diversity of the members, clients and communities we serve.

If there''s something we can do to help make the recruitment process or the job you''re applying for more accessible, let us know. We can provide accommodations at any stage in the recruitment process. Just ask!

Job Family
Information technology (FG)

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:50:56.289165', true, 32);
INSERT INTO public.raw_postings VALUES (27, 'jsearch', 'https://grabjobs.co/canada/job/internship/others/summer-interncoop-2026-communications-and-design-152263674?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic', 'Job Title: Summer Intern/Co-op 2026  Communications / Design
Company: Manulife
Location: Montreal, Quebec CA
Employment Type: Internship
Posted: 2026-01-11T01:00:00.000Z

Salary: Not specified

Description:
Join our Global Cybersecurity (GCS) Team as a Communications & Design Intern and play a key role in centralizing resources, supporting internal campaigns, and creating branded assets that align with Manulife’s standards. This role combines creativity, technology, and collaboration to deliver impactful solutions.

Position Responsibilities:
• Design and develop a SharePoint site to centralize GCS resources and updates.
• Create branded templates and visual assets aligned with Manulife’s brand standards.
• Support internal communication campaigns and culture initiatives.
• Coordinate 2026 cybersecurity training sessions with vendors and internal stakeholders.
• Assist with day-to-day administrative and creative tasks to enable strategic priorities.
• Collaborate with cybersecurity and communications teams to deliver high-quality content.

Required Qualifications:
• Currently pursuing an undergraduate degree in Communications, Graphic Design, Digital Media, Marketing, Information Technology, Web Design/Development, Cybersecurity, or a related field.
• Strong proficiency in Microsoft Office tools.
• Experience with graphic design tools.
• Familiarity with branding principles and digital marketing concepts.
• Knowledge of web design or SharePoint customization.
• Ability to share a portfolio showcasing design and communication work.

Preferred Qualifications:
• Exceptional verbal and written communication skills.
• Interest in technology.

When you join our team:
• We’ll empower you to learn and grow the career you want.
• We’ll recognize and support you in a flexible environment where well-being and inclusion are more than just words.
• As part of our global team, we’ll support you in shaping the future you want to see.

Application instructions:
• Submit your resume, cover letter, academic transcript, and work term evaluation (if any) in one PDF file.
• Note: Applications are reviewed on a rolling basis.

#LI-Hybrid

About Manulife and John Hancock

Manulife Financial Corporation is a leading international financial services provider, helping people make their decisions easier and lives better. To learn more about us, visit https://www.manulife.com/en/about/our-story.html.

Manulife is an Equal Opportunity Employer

At Manulife/John Hancock, we embrace our diversity. We strive to attract, develop and retain a workforce that is as diverse as the customers we serve and to foster an inclusive work environment that embraces the strength of cultures and individuals. We are committed to fair recruitment, retention, advancement and compensation, and we administer all of our practices and programs without discrimination on the basis of race, ancestry, place of origin, colour, ethnic origin, citizenship, religion or religious beliefs, creed, sex (including pregnancy and pregnancy-related conditions), sexual orientation, genetic characteristics, veteran status, gender identity, gender expression, age, marital status, family status, disability, or any other ground protected by applicable law.

It is our priority to remove barriers to provide equal access to employment. A Human Resources representative will work with applicants who request a reasonable accommodation during the application process. All information shared during the accommodation request process will be stored and used in a manner that is consistent with applicable laws and Manulife/John Hancock policies. To request a reasonable accommodation in the application process, contact recruitment@manulife.com.

Working Arrangement
Hybrid

Original job Summer Intern/Co-op 2026 Communications / Design posted on GrabJobs ©. To flag any issues with this job please use the Report Job button on GrabJobs.

Required Skills/Qualifications:
[''Not specified'']', '2026-01-11 09:50:56.647747', true, 33);


--
-- Name: companies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: snitil
--

SELECT pg_catalog.setval('public.companies_id_seq', 34, true);


--
-- Name: jobs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: snitil
--

SELECT pg_catalog.setval('public.jobs_id_seq', 33, true);


--
-- Name: raw_postings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: snitil
--

SELECT pg_catalog.setval('public.raw_postings_id_seq', 27, true);


--
-- Name: skills_id_seq; Type: SEQUENCE SET; Schema: public; Owner: snitil
--

SELECT pg_catalog.setval('public.skills_id_seq', 60, true);


--
-- PostgreSQL database dump complete
--

\unrestrict oP8EJnfwWDkNY72dyVi8K5AuvHbQYUyLwCu9Z1VWi1sIfytIlERDF51Na9xWslb

