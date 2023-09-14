# $NetBSD$

DISTNAME=	mip-1.15.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel
MASTER_SITES=	${MASTER_SITE_PYPI:=m/mip/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/mip/
COMMENT=	tools for modeling and solution of Mixed-Integer Linear programs
LICENSE=	epl-v2.0

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
DEPENDS+=	${PYPKGPREFIX}-cffi>=1.15:../../devel/py-cffi
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.24:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-test>=7.2.0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-networkx>=2.8.8:../../math/py-networkx
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=3.6.2:../../graphics/py-matplotlib

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
