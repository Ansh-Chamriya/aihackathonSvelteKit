import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

function generateRandomText(wordCount: number): string {
    const words = [
        "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
        "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
        "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud",
        "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea",
        "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit",
        "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla",
        "pariatur", "excepteur", "sint", "occaecat", "cupidatat", "non", "proident",
        "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum"
    ];

    let randomText = '';
    for (let i = 0; i < wordCount; i++) {
        const randomIndex = Math.floor(Math.random() * words.length);
        randomText += words[randomIndex] + ' ';
    }

    return randomText.trim();
}

export const POST: RequestHandler = async ({ request }) => {
    const { prompt } = await request.json();
    const response = await fetch(
        "https://bxdwqjsk-8000.inc1.devtunnels.ms/predict",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "allow-acess-control-origin": "*",
            },

            body: JSON.stringify({ description: prompt }),
        }
    );
    const responseText = await response.text();
    console.log("response:", response, responseText);


    return json({ responseText }, { status: 201 });
};