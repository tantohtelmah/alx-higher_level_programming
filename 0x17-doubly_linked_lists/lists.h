#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>
#include <stdio.h>

typedef struct dlistint_t
{
	int n;
	struct dlistint_t *next;
	struct dlistint_t *prev;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h);

#endif /* LISTS_H */
