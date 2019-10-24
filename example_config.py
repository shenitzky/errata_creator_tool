"""
Example configuration module.
"""

# Dictionary of projects.
#
# Here is an example of project configuration that providing all
# the needed fields for the errata.

PROJECTS = {

    "ioprocess": {
        'product': 'RHV',
        'synopsis': 'Red Hat Ceph Storage 2.1 bug fix update',
        'topic': 'An update for Red Hat Ceph 2.1 is now available.',
        'description': 'This update contains the following fixes ...',
        'solution': 'Before applying this update...',
        'qe_email': 'qa-errata-list@redhat.com',
        'qe_group': 'RHEVM QE',
        'owner_email': 'eshenitz@redhat.com',
        'manager_email': 'ship-list@redhat.com',
    },

}
