"""Tests for the hierarchical clustering class."""

import unittest

import pandas as pd

from lta.cores.cpa.clustering.hierarchical import HierarchicalClustering


class TestHierarchicalClustering(unittest.TestCase):
    """Unit tests for the HierarchicalClustering class."""

    def setUp(self) -> None:
        """Set up the test data and the HierarchicalClustering object."""
        self.number_clusters = 2
        self.data = pd.DataFrame(
            {
                "feature1": [1, 2, 3, 4, 5],
                "feature2": [5, 4, 3, 2, 1],
                "feature3": [2, 3, 4, 5, 6],
            }
        )
        self.hc = HierarchicalClustering(number_clusters=self.number_clusters)

    def test_cluster(self) -> None:
        """Test the cluster method."""
        clusters = self.hc.cluster(self.data)
        cluster_labels = set(range(self.number_clusters))
        self.assertEqual(len(clusters), self.data.shape[0])
        self.assertTrue(all(cluster in cluster_labels for cluster in clusters))
