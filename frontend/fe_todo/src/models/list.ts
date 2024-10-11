import { User } from './account'

export type ListData = {
  id: number,
  user: User,
  user_id: number,
  list_name: string,
};

export type ListResponse = {
  list_name : string,
}