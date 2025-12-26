# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-science-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for natural sciences
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# graphics
DEPENDS+=	gnuplot>=0:../../graphics/gnuplot
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib

# math
DEPENDS+=	basic-stats>=0:../../math/basic-stats
#DEPENDS+=	octave>=0:../../math/octave
DEPENDS+=	${PYPKGPREFIX}-lmfit>=0:../../math/py-lmfit
DEPENDS+=	${PYPKGPREFIX}-mpmath>=0:../../math/py-mpmath
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-scikit-image>=0:../../math/py-scikit-image
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=0:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-sympy>=0:../../math/py-sympy
#DEPENDS+=	${PYPKGPREFIX}-torch>=0:../../math/py-torch
DEPENDS+=	${PYPKGPREFIX}-uncertainties>=0:../../math/py-uncertainties
DEPENDS+=	qcalc>=0:../../math/qcalc

# pkgsrc_myownpkgs
DEPENDS+=	${PYPKGPREFIX}-fastavro>=0:../../pkgsrc_myownpkgs/py-fastavro
DEPENDS+=	flatbuffers>=0:../../pkgsrc_myownpkgs/flatbuffers
DEPENDS+=	apache-arrow>=0:../../wip/apache-arrow
DEPENDS+=	${PYPKGPREFIX}-apache-arrow>=0:../../pkgsrc_myownpkgs/py-apache-arrow
DEPENDS+=	${PYPKGPREFIX}-setuptools-git-versioning>=0:../../pkgsrc_myownpkgs/py-setuptools-git-versioning
DEPENDS+=	${PYPKGPREFIX}-bokeh>=0:../../pkgsrc_myownpkgs/py-bokeh
DEPENDS+=	${PYPKGPREFIX}-tblib>=0:../../pkgsrc_myownpkgs/py-tblib
DEPENDS+=	${PYPKGPREFIX}-distributed>=0:../../pkgsrc_myownpkgs/py-distributed
DEPENDS+=	${PYPKGPREFIX}-ndindex>=0:../../pkgsrc_myownpkgs/py-ndindex
#DEPENDS+=	${PYPKGPREFIX}-blosc2>=0:../../pkgsrc_myownpkgs/py-blosc2
#DEPENDS+=	${PYPKGPREFIX}-partd>=0:../../pkgsrc_myownpkgs/py-partd
#DEPENDS+=	${PYPKGPREFIX}-dask>=0:../../pkgsrc_myownpkgs/py-dask
DEPENDS+=	${PYPKGPREFIX}-pint>=0:../../pkgsrc_myownpkgs/py-pint
DEPENDS+=	${PYPKGPREFIX}-plotly>=0:../../pkgsrc_myownpkgs/py-plotly
DEPENDS+=	${PYPKGPREFIX}-geodatasets>=0:../../pkgsrc_myownpkgs/py-geodatasets
DEPENDS+=	${PYPKGPREFIX}-geopandas>=0:../../pkgsrc_myownpkgs/py-geopandas

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
