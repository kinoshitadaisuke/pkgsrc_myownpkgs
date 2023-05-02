# $NetBSD$

DISTNAME=	scikit_build-0.17.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/scikit_build/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/scikit_build/
COMMENT=	Improved build system generator for CPython
LICENSE=	mit

USE_LANGUAGES=	c++

DEPENDS+=	${PYPKGPREFIX}-hatchling>=1.4:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-hatch-fancy-pypi-readme>0:../../devel/py-hatch-fancy-pypi-readme
DEPENDS+=	${PYPKGPREFIX}-hatch-vcs>0:../../devel/py-hatch-vcs
DEPENDS+=	${PYPKGPREFIX}-distro>0:../../devel/py-distro
DEPENDS+=	${PYPKGPREFIX}-packaging>0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-setuptools>=42.0.0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-tomli>0:../../textproc/py-tomli
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=3.7:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-wheel>=0.32.0:../../devel/py-wheel

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
