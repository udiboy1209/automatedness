import { defineCollection, z } from 'astro:content';

const main = defineCollection({
    schema: z.object({
        title: z.string(),
        order: z.number(),
    }),
});

const schema = z.object({
    title: z.string(),
    date: z.date(),
    featured: z.boolean().optional(),
    summary: z.string().optional(),
    image: z.string().optional(),
    link: z.string().optional(),
    tag: z.string().optional(),
    category: z.string().optional()
})

const projects = defineCollection({schema: schema});
const blog = defineCollection({schema: schema});

export const collections = { main, projects, blog };
