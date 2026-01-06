# $NetBSD$

DISTNAME=	pyspark_connect-4.1.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pyspark_connect/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/apache/spark/tree/master/python
COMMENT=	Apache Spark Python API with Spark Connect by default
LICENSE=	apache-2.0

DEPENDS+=	${PYPKGPREFIX}-apache-arrow>=11.0.0:../../pkgsrc_myownpkgs/py-apache-arrow
DEPENDS+=	${PYPKGPREFIX}-googleapis-common-protos>=1.71.0:../../devel/py-googleapis-common-protos
DEPENDS+=	${PYPKGPREFIX}-grpcio>=1.76.0:../../net/py-grpcio
DEPENDS+=	${PYPKGPREFIX}-pandas>=2.0.0:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-yaml>=3.11:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-zstandard>=0.25.0:../../archivers/py-zstandard
DEPENDS+=	${PYPKGPREFIX}-grpcio-status>=1.76.0:../../pkgsrc_myownpkgs/py-pyspark-connect
#DEPENDS+=	${PYPKGPREFIX}-pyspark>=4.1.0:../../pkgsrc_myownpkgs/py-pyspark

USE_LANGUAGES=	# none

#BUILDLINK_API_DEPENDS.py-numpy+=	${PYPKGPREFIX}-numpy>=1.21

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
