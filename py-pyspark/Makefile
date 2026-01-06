# $NetBSD$

DISTNAME=	pyspark-4.1.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pyspark/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pyspark/
COMMENT=	Apache Spark Python API
LICENSE=	apache-2.0

# dependencies
DEPENDS+=	${PYPKGPREFIX}-py4j>=0.10.9.9:../../pkgsrc_myownpkgs/py-py4j
# optional dependencies
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.22:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-apache-arrow>=18.0.0:../../pkgsrc_myownpkgs/py-apache-arrow
DEPENDS+=	${PYPKGPREFIX}-six>=1.16.0:../../lang/py-six
DEPENDS+=	${PYPKGPREFIX}-pandas>=2.2:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-plotly>=6.0.0:../../pkgsrc_myownpkgs/py-plotly
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=0:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-memory-profiler>=0.61.0:../../devel/py-memory-profiler
DEPENDS+=	${PYPKGPREFIX}-yaml>=3.11:../../textproc/py-yaml

# url2pkg-marker (please do not remove this line.)
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
