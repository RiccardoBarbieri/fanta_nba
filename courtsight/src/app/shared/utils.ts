export function getFormattedDate(date: Date)
{
  return date.toISOString().split('T')[0];
}
