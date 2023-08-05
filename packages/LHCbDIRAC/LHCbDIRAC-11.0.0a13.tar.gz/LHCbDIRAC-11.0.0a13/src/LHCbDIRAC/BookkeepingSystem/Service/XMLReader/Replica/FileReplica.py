###############################################################################
# (c) Copyright 2019 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "LICENSE".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
"""stores the file parameters."""
from LHCbDIRAC.BookkeepingSystem.Service.XMLReader.Replica.Replica import Replica


class FileReplica(Replica):
    """FileReplica class."""

    def writeToXML(self):
        """creates an xml string."""
        result = ""
        for param in self.params:
            result += param.writeToXML()

        return result
