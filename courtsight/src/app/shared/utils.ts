export function getFormattedDate(date: Date)
{
  return date.toISOString().split('T')[0];
}

export function counterArray(n: number): any[] {
  return Array(n);
}
