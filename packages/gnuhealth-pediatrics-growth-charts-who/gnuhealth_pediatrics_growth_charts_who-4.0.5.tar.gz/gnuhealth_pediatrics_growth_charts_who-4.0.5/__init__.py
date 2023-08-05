##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2022 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2013 Sebastián Marro <smarro@thymbra.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from trytond.pool import Pool
from . import health_pediatrics_growth_charts_who
from . import wizard
from . import report


def register():
    Pool.register(
        health_pediatrics_growth_charts_who.PediatricsGrowthChartsWHO,
        wizard.wizard_health_pediatrics_growth_charts_who.
        OpenPediatricsGrowthChartsWHOReportStart,
        module='health_pediatrics_growth_charts_who', type_='model')
    Pool.register(
        wizard.wizard_health_pediatrics_growth_charts_who.
        OpenPediatricsGrowthChartsWHOReport,
        module='health_pediatrics_growth_charts_who', type_='wizard')
    Pool.register(
        report.report_health_pediatrics_growth_charts_who.
        PediatricsGrowthChartsWHOReport,
        report.report_health_pediatrics_growth_charts_who.
        WeightForAge,
        report.report_health_pediatrics_growth_charts_who.
        LengthHeightForAge,
        report.report_health_pediatrics_growth_charts_who.
        BMIForAge,
        module='health_pediatrics_growth_charts_who', type_='report')
