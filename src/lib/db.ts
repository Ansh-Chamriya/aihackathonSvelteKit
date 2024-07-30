import Dexie, { type Table } from "dexie";
interface chats {
    id?: number;
    prompt: string;
    response: string;
    cretaedAt: Date;
}

export class chatbucket extends Dexie {
    chats!: Table<chats>;

    constructor() {
        super('chatbucket');

        this.version(1).stores({
            chats: '++id, prompt, response, cretaedAt'
        })

    }
}

export const db = new chatbucket();