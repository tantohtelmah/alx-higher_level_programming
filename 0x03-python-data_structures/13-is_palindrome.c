#include "lists.h"

/**
* is_palindrome - checks is a word is a palindrome
* @head: listint_t
* Return: int
*/
void reverse_list(listint_t **head);
int compare_lists(listint_t *head1, listint_t *head2);

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL;
	listint_t *second_half = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			slow = slow->next;
		}

		second_half = slow;
		prev->next = NULL;
		reverse_list(&second_half);
		res = compare_lists(*head, second_half);
		reverse_list(&second_half);

		if (fast != NULL)
		{
			prev->next = slow;
			slow->next = second_half;
		}
		else
		{
			prev->next = second_half;
		}
	}

	return (res);
}
/**
* reverse_list - checks is a word is a palindrome
* @head: listint_t
* Return: int
*/
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}
/**
* compare_lists - compares two lists
* @head1: listint_t
* @head2: listint_t
* Return: int
*/
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1, *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}

	return (0);
}
