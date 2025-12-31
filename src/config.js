import { Github, Linkedin, GraduationCap, Mail } from '@lucide/astro';

export const SITE_NAME = "Meet Udeshi"
export const NAV_LINKS = [
    {link: '/index.html#about', name: 'About'},
    {link: '/index.html#publications', name: 'Publications'},
    {link: '/projects/', name: 'Projects'},
    {link: '/pdfs/cv_one_page.pdf', name: 'CV'},
    {link: '/blog/', name: 'Blog'},
];
export const SOCIAL_LINKS = [
    {link: 'https://github.com/udiboy1209', name: 'github', icon: Github},
    {link: 'https://www.linkedin.com/in/meet-udeshi-10a51baa/', name: 'linked-in', icon: Linkedin},
    {link: 'https://scholar.google.com/citations?user=YlIc4EQAAAAJ&hl=en', name: 'google scholar', icon: GraduationCap},
    {link: 'mailto:m.udeshi@nyu.edu', name: 'email', icon: Mail},
]
