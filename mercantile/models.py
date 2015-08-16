from django.db import models
from django.utils.translation import ugettext_lazy as _

from waffles.models import Event, UserProfile


class Debt(models.Model):
    """
    The total debt owed by debtor to debtee.

    If system is consistent this will be the sum of calculation.amount
    and settlement.amount
    """
    amount = models.BigIntegerField(verbose_name=_("Amount owed"))
    debtor = models.ForeignKey(UserProfile, related_name="debtor", verbose_name=_("Debtor"))
    debtee = models.ForeignKey(UserProfile, related_name="debtee", verbose_name=_("Debtee"))

    class Meta:
        verbose_name = _('Total debt')
        verbose_name_plural = _('Total debts')


class Calculation(models.Model):
    """
    This is a single calculation of debt from an event.
    """
    debt = models.ForeignKey(Debt, verbose_name=_("Connected debt"))
    event = models.ForeignKey(Event, _("Connected event"))
    amount = models.IntegerField(verbose_name=_("Amount owed"))
    date = models.DateTimeField(verbose_name=_("Date integrated"))

    class Meta:
        verbose_name = _('Calculation')
        verbose_name_plural = _('Calculations')


class Settlement(models.Model):
    """
    When part of or a whole debt is settled in 'cash'
    """
    debt = models.ForeignKey(Debt, verbose_name=_("Connected debt"))
    date = models.DateField(verbose_name=_("Date made"))
    amount = models.IntegerField(verbose_name=_("Amount owed"))

    class Meta:
        verbose_name = _('Cash settlement')
        verbose_name_plural = _('Cash settlements')
